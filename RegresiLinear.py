import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

#Membaca file dataset
def load_df(file_path):
    df = pd.read_excel(file_path)
    return df

#Melakukan prediksi dengan regresi linear
def predict(df):
    X = df[['Nilai Ulangan Harian', 'Nilai Ujian Tengah Semester', 'Nilai Ujian Akhir Semester', 'Konversi (Menit)']]
    y = df['Nilai Akhir']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    st.write("Mean Squared Error:", mse)
    st.write("R^2 Score:", r2)

    #Menampilkan graph plot nilai perbandingan aktual dengan prediksi
    fig, ax = plt.subplots()
    ax.scatter(y_test, y_pred)
    ax.set_xlabel("Nilai Aktual")
    ax.set_ylabel("Nilai Prediksi")
    ax.set_title("Nilai Aktual vs. Prediksi")
    st.pyplot(fig)

#Membuat tampilan
def main():
    st.title("Regresi Linier App")
    st.write("Aplikasi untuk melakukan prediksi menggunakan Regresi Linier")

    
    uploaded_file = st.file_uploader("Pilih df (format: .xlsx)", type="xlsx")

    if uploaded_file:
        df = load_df(uploaded_file)
        st.write("Data:", df.head(10))

        if st.button("Prediksi"):
            predict(df)

if __name__ == '__main__':
    main()
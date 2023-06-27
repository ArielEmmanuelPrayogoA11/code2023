import tkinter as tk
from tkinter import filedialog
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Fungsi untuk membaca dataset
def load_dataset():
    file_path = filedialog.askopenfilename(filetypes=[('Excel Files', '*.xlsx')])
    dataset = pd.read_excel(file_path)
    return dataset

# Fungsi untuk melakukan prediksi dan menampilkan hasil
def predict():
    dataset = load_dataset()
    X = dataset[['Nilai Ulangan Harian', 'Nilai Ujian Tengah Semester', 'Nilai Ujian Akhir Semester', 'Konversi (Menit)']]
    y = dataset['Nilai Akhir']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    result_label.config(text=f"Mean Squared Error: {mse}\nR^2 Score: {r2}")

    # Menampilkan plot nilai aktual vs. prediksi
    fig, ax = plt.subplots()
    ax.scatter(y_test, y_pred)
    ax.set_xlabel("Nilai Aktual")
    ax.set_ylabel("Nilai Prediksi")
    ax.set_title("Nilai Aktual vs. Prediksi")
    plt.show()

# Membuat tampilan GUI menggunakan Tkinter
root = tk.Tk()
root.title("Regresi Linier App")

# Tombol untuk memilih dataset
load_button = tk.Button(root, text="Pilih Dataset", command=load_dataset)
load_button.pack(pady=10)

# Tombol untuk melakukan prediksi
predict_button = tk.Button(root, text="Prediksi", command=predict)
predict_button.pack(pady=10)

# Label untuk menampilkan hasil
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()

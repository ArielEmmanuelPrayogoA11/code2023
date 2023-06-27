import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Fungsi untuk membaca dataset
def open_dataset():
    file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    if file_path:
        try:
            dataset = pd.read_excel(file_path)
            return dataset
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open dataset: {e}")
    return None

# Fungsi untuk memprediksi dan menampilkan hasil
def predict():
    dataset = open_dataset()
    if dataset is not None:
        try:
            X = dataset[['Nilai Ulangan Harian', 'Nilai Ujian Tengah Semester', 'Nilai Ujian Akhir Semester', 'Awal Mengerjakan', 'Akhir Mengerjakan', 'Durasi Mengerjakan', 'Konversi (Menit)']]
            y = dataset['Nilai Akhir']

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            model = LinearRegression()
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)

            mse = mean_squared_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)

            messagebox.showinfo("Prediction Result", f"Mean Squared Error: {mse}\nR^2 Score: {r2}")

            # Menampilkan plot nilai aktual vs. prediksi
            plt.scatter(y_test, y_pred)
            plt.xlabel("Nilai Aktual")
            plt.ylabel("Nilai Prediksi")
            plt.title("Nilai Aktual vs. Prediksi")
            plt.show()

        except Exception as e:
            messagebox.showerror("Error", f"Failed to predict: {e}")

# Fungsi untuk menampilkan dialog tentang aplikasi
def about():
    messagebox.showinfo("About", "Linear Regression App\n\nAplikasi untuk melakukan prediksi menggunakan Regresi Linier.")

# Membuat jendela GUI
window = tk.Tk()
window.title("Linear Regression App")

# Membuat tombol untuk membuka dataset
open_button = tk.Button(window, text="Open Dataset", command=open_dataset)
open_button.pack(pady=10)

# Membuat tombol untuk memprediksi
predict_button = tk.Button(window, text="Predict", command=predict)
predict_button.pack(pady=10)

# Membuat tombol untuk informasi tentang aplikasi
about_button = tk.Button(window, text="About", command=about)
about_button.pack(pady=10)

# Menjalankan aplikasi
window.mainloop()

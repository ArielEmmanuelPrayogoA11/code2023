# -*- coding: utf-8 -*-
"""DataMiningNeuralNetwork.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IClynkuuXzOkiXmerrnhtRJHlp9VIQQp
"""

# Ariel Emmanuel Prayogo - A11.2020.12535 - 4618

import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import optimizers, losses
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

# Membaca dataset dari file xlsx
df = pd.read_excel('NilaiAkhir.xlsx')
df.head(10)

# Deskripsi Dataset
print(df.describe())

# Cek tipe data pada tiap kolom
print(df.dtypes)

# Mengubah Nilai Akhir menjadi Float dan Menghapus Kolom yang tidak diperlukan
df['Nilai Akhir'] = df['Nilai Akhir'].astype(float)
df = df.drop('No', axis=1)

# Cek Ulang
print(df.dtypes)

# Mencari Data Kosong
df.isnull().sum()

# Konversi (Menit) berisikan data durasi pengerjaan yang sudah di konversi menjadi menit
# Data ini diubah ke Satuan Jam dan dikali 100
df['Konversi (Menit)'] = (df['Konversi (Menit)'] / 60) * 100

print(df.describe()) # Cek Ulang Data , apakah sudah berhasil diubah

# Cek Ulang Tipe Data , Pastikan sudah Float
print(df.dtypes)

# Split atribut dengan target/label
features = df[['Nilai Ulangan Harian', 'Nilai UTS','Nilai UAS','Nilai Akhir']].values
label = df['Konversi (Menit)'].values

# Normalisasi data untuk mempermudah komputasi
normalized_label = label/100
normalized_features = features/100

print(normalized_features)

# Cek data yang sudah dinormalisasi
print(normalized_label)

# Metode Neural Network

# Membuat objek model Sequential
model = Sequential()
# Menambahkan layer Dense dengan 1 neuron dan input shape 4 sesuai dengan jumlah atribut
model.add(Dense(1, input_shape=(4,)))

# Mengompilasi model dengan optimizer 'SGD' (Stochastic Gradient Descent) dan loss function 'MSE' (Mean Squared Error)
model.compile(optimizer='sgd', loss='mse')

# Melatih model menggunakan fit() epochs=1000
history=model.fit(normalized_features,normalized_label, epochs=1000)

# Fungsi Prediksi
def predict_time():
# Data yang di inputkan akan di normalisasi dengan dibagikan 100 agar nilai tetap sama
  nilai_ujian = float(input("Input Nilai Ujian: "))/100
  nilai_uts = float(input("Input Nilai UTS: "))/100
  nilai_uas = float(input("Input Nilai UAS: "))/100
  nilai_akhir = float(input("Input Nilai Akhir: "))/100



  input_data = [[nilai_ujian, nilai_uts,nilai_uas,nilai_akhir]]
  prediction = model.predict(input_data)


  waktu_pengerjaan = prediction[0][0] * 60
  print("Prediksi waktu pengerjaan: {:.2f} menit".format(waktu_pengerjaan))
  print("Atau Kurang Lebih {:.0f} menit".format(waktu_pengerjaan))

# Pemanggilan Fungsi
predict_time()
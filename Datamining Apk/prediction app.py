import tkinter as tk
from tkinter import messagebox
from tensorflow.keras.models import load_model

def predict_time(model):
    nilai_ujian = float(entry_ujian.get())/100
    nilai_uts = float(entry_uts.get())/100
    nilai_uas = float(entry_uas.get())/100
    nilai_akhir = float(entry_akhir.get())/100
    
    input_data = [[nilai_ujian, nilai_uts, nilai_uas, nilai_akhir]]
    prediction = model.predict(input_data)
    
    waktu_pengerjaan = prediction[0][0] * 60
    messagebox.showinfo("Prediction Result", "Prediksi waktu pengerjaan: {:.2f} menit\nAtau Kurang Lebih {:.0f} menit".format(waktu_pengerjaan, waktu_pengerjaan))

# Load the trained model
model = load_model("dataminingneuralnetwork.py")

# Create tkinter window
window = tk.Tk()
window.title("Prediction App")

# Rest of the code remains the same
# ...

# Start the GUI event loop
window.mainloop()
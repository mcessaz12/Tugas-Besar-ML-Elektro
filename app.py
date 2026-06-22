import streamlit as st
import joblib
import numpy as np

# Load Model yang tadi didownload
model = joblib.load('model_mesin_elektro.pkl')

# Desain Antarmuka Web App
st.title("Aplikasi Prediksi Kondisi Mesin")
st.write("Masukkan parameter sensor di bawah ini untuk melihat hasil prediksi.")

# Input Form untuk User
tegangan = st.number_input("Tegangan (Volt)", min_value=0.0, value=220.0)
arus = st.number_input("Arus (Ampere)", min_value=0.0, value=10.0)

# Tombol Prediksi
if st.button("Prediksi Sekarang"):
    # Ubah input menjadi format yang bisa dibaca model (array 2D)
    input_data = np.array([[tegangan, arus]])
    
    # Lakukan prediksi
    hasil = model.predict(input_data)
    
    # Tampilkan hasil (0 = Normal, 1 = Rusak dari data latihan kita sebelumnya)
    if hasil[0] == 0:
        st.success("Hasil Prediksi: Mesin dalam kondisi NORMAL")
    else:
        st.error("Hasil Prediksi: Mesin terdeteksi RUSAK!")
import streamlit as st
import joblib
import numpy as np

# 1. Load Model Smart Grid yang baru
model = joblib.load('model_smart_grid.pkl')

# 2. Desain Antarmuka Web App
st.set_page_config(page_title="Smart Grid Predictor", layout="centered")
st.title("⚡ Prediksi Stabilitas Smart Grid")
st.write("Aplikasi ini menggunakan Machine Learning (Random Forest) untuk memprediksi apakah jaringan tenaga listrik pintar akan stabil atau tidak berdasarkan parameter node.")

st.markdown("---")
st.subheader("Masukkan Parameter Sensor Jaringan:")

# Membuat kolom agar tampilan web lebih rapi (3 kolom)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Waktu Reaksi (Tau)**")
    tau1 = st.number_input("Tau 1", value=2.50)
    tau2 = st.number_input("Tau 2", value=2.50)
    tau3 = st.number_input("Tau 3", value=2.50)
    tau4 = st.number_input("Tau 4", value=2.50)

with col2:
    st.markdown("**Keseimbangan Daya (P)**")
    p1 = st.number_input("P 1", value=3.50)
    p2 = st.number_input("P 2", value=-1.00)
    p3 = st.number_input("P 3", value=-1.00)
    p4 = st.number_input("P 4", value=-1.00)

with col3:
    st.markdown("**Elastisitas Harga (G)**")
    g1 = st.number_input("G 1", value=0.50)
    g2 = st.number_input("G 2", value=0.50)
    g3 = st.number_input("G 3", value=0.50)
    g4 = st.number_input("G 4", value=0.50)

st.markdown("---")

# 3. Tombol Prediksi
if st.button("🔌 Prediksi Stabilitas Jaringan", use_container_width=True):
    # Gabungkan semua input menjadi array 2D yang bisa dibaca model
    input_data = np.array([[tau1, tau2, tau3, tau4, p1, p2, p3, p4, g1, g2, g3, g4]])
    
    # Lakukan prediksi
    hasil = model.predict(input_data)
    
    # Tampilkan hasil (0 = Unstable, 1 = Stable)
    if hasil[0] == 1:
        st.success("✅ HASIL PREDIKSI: JARINGAN STABIL (STABLE)")
    else:
        st.error("⚠️ HASIL PREDIKSI: JARINGAN TIDAK STABIL (UNSTABLE)")

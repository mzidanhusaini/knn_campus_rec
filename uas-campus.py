import pickle
import streamlit as st
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder


# Load the KNN model
with open('KNN_campus.sav', 'rb') as file:
    knn_model = pickle.load(file)

st.title("Prediksi Seleksi Kampus")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox('Jenis Kelamin', ['Laki-Laki', 'Perempuan'])
    hsc_b = st.selectbox('Dewan Pendidikan- Pusat/ Lainnya', ['Central', 'Others'])
    hsc_s = st.selectbox('Peminatan dalam Pendidikan Menengah Atas', ['Commerce', 'Science', 'Arts'])
    degree_t = st.selectbox('Di bawah Kelulusan (Jenis gelar) - Bidang pendidikan gelar', ['Sci&Tech', 'Comm&Mgmt', 'Others'])
    workex = st.selectbox('Pengalaman Kerja', ['No', 'Yes'])
    salary = st.selectbox('Gaji yang ditawarkan oleh perusahaan kepada kandidat', ['rendah', 'sedang', 'tinggi'])
    specialisation = st.selectbox('Pasca Sarjana (MBA) - Spesialisasi', ['Mkt&HR', 'Mkt&Fin'])

with col2:
    ssc_p = st.number_input('Persentase Pendidikan Menengah - Kelas 10')
    hsc_p = st.number_input('Persentase Pendidikan Menengah Atas- Kelas 12')
    degree_p = st.number_input('Persentase Gelar')
    etest_p = st.number_input('Persentase tes kemampuan kerja (dilakukan oleh perguruan tinggi)')
    mba_p = st.number_input('Persentase MBA')
    
# Fungsi untuk melakukan label encoding pada satu kolom
def label_encode_column(le, column_data):
    encoded_data = le.transform([column_data])[0]
    return encoded_data

# Melakukan label encoding untuk setiap kolom
le_gender, _ = label_encode_column(*encoded_gender)
le_hsc_b, _ = label_encode_column(*encoded_hsc_b)
le_hsc_s, _ = label_encode_column(*encoded_hsc_s)
le_degree_t, _ = label_encode_column(*encoded_degree_t)
le_workex, _ = label_encode_column(*encoded_workex)
le_salary, _ = label_encode_column(*encoded_salary)
le_specialisation, _ = label_encode_column(*encoded_specialisation)

predict = ''

if st.button('Prediksi'):
    # Note: Pass a single 2D array with the encoded values
    input_data = [[le_gender, le_hsc_b, le_hsc_s, le_degree_t,
                   le_workex, le_salary, le_specialisation, ssc_p,
                   hsc_p, degree_p, etest_p, mba_p]]

    predict = knn_model.predict(input_data)

    if predict == 0:
        predict = "Kandidat Lolos"
    else:
        predict = "Kandidat Tidak Lolos"

    st.write(predict)

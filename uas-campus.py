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
def label_encode_column(column_data):
    le = LabelEncoder()
    encoded_data = le.fit_transform(column_data)
    return le, encoded_data

# Melakukan label encoding untuk setiap kolom
encoded_gender = label_encode_column(['Laki-Laki', 'Perempuan'])
encoded_hsc_b = label_encode_column(['Central', 'Others'])
encoded_hsc_s = label_encode_column(['Commerce', 'Science', 'Arts'])
encoded_degree_t = label_encode_column(['Sci&Tech', 'Comm&Mgmt', 'Others'])
encoded_workex = label_encode_column(['No', 'Yes'])
encoded_salary = label_encode_column(['rendah', 'sedang', 'tinggi'])
encoded_specialisation = label_encode_column(['Mkt&HR', 'Mkt&Fin'])

predict = ''

if st.button('Prediksi'):
    predict = knn_model.predict([[encoded_gender,encoded_hsc_b,encoded_hsc_s,encoded_degree_t,
                                  encoded_workex,encoded_salary,encoded_specialisation,ssc_p,
                                  hsc_p,degree_p,etest_p,mba_p]])
    
    if predict == 0:
        predict = "Kandidat Lolos"
    else:
        predict = "Kandidat Tidak Lolos"

    st.write(predict)

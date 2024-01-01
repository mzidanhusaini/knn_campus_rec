import pickle
import streamlit as st
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier


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
    
label_encoder_gender = LabelEncoder()
label_encoder_gender.fit(['Laki-Laki', 'Perempuan'])
encoded_gender = label_encoder_gender.transform([gender])[0]

label_encoded_hsc_b = LabelEncoder()
label_encoded_hsc_b.fit(['Central', 'Others'])
encoded_hsc_b = label_encoded_hsc_b.transform([hsc_b])[0]

label_encoded_hsc_s = LabelEncoder()
label_encoded_hsc_s.fit(['Commerce', 'Science', 'Arts'])
encoded_hsc_s = label_encoded_hsc_s.transform([hsc_s])[0]

label_encoded_degree_t = LabelEncoder()
label_encoded_degree_t.fit(['Sci&Tech', 'Comm&Mgmt', 'Others'])
encoded_degree_t = label_encoded_degree_t.transform([degree_t])[0]

label_encoded_workex = LabelEncoder()
label_encoded_workex.fit(['No', 'Yes'])
encoded_workex = label_encoded_workex.transform([workex])[0]

label_encoded_salary = LabelEncoder()
label_encoded_salary.fit(['rendah', 'sedang', 'tinggi'])
encoded_salary = label_encoded_salary.transform([salary])[0]

label_encoded_specialisation = LabelEncoder()
label_encoded_specialisation.fit(['Mkt&HR', 'Mkt&Fin'])
encoded_specialisation = label_encoded_specialisation.transform([specialisation])[0]

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

# Laporan Proyek Machine Learning
### Nama : Muhamad Zidan Husaini
### Nim : 211351092
### Kelas : Pagi B

## Domain Proyek

Rekrutmen kampus adalah strategi untuk mencari, menarik, dan merekrut talenta muda untuk posisi magang dan level pemula. Perekrutan kampus biasanya merupakan taktik untuk perusahaan menengah hingga besar dengan kebutuhan perekrutan bervolume tinggi, tetapi dapat berkisar dari upaya kecil (seperti bekerja dengan pusat karir universitas untuk mencari kandidat potensial) hingga operasi skala besar (seperti mengunjungi beragam perguruan tinggi dan menghadiri acara perekrutan sepanjang musim semi dan musim gugur). Perekrutan kampus sering kali melibatkan kerja sama dengan pusat layanan karier universitas dan menghadiri pameran karier untuk bertemu langsung dengan mahasiswa dan lulusan baru.

## Business Understanding

Berdasarkan domain projek tersebut maka pembuatan sistem yang membantu dalam proses klasifikasi penempatan mahasiswa di dunia industri akan menjadi hal yang baik dan berguna.

Bagian laporan ini mencakup:

### Problem Statements

Menjelaskan pernyataan masalah latar belakang:
- Faktor apa yang mempengaruhi seorang kandidat untuk ditempatkan?
- Apakah persentase penting bagi seseorang untuk ditempatkan?
- Spesialisasi gelar apa yang banyak diminati oleh perusahaan?

### Goals

Menjelaskan tujuan dari pernyataan masalah:
- dapat mengetahui faktor yang mempengaruhi seorang kandidat dalam proses penempatan kerja
- mengetahui persentase dari atribut tersebut apakah lolos atau tidak
- mengetahui spesialisasi gelar apa yang paling banyak di minati perusahaan

    ### Solution statements
    - Pembuatan model dan sistem yang mempermudah dalam proses klasifikasi
    - metrik evaluasi yang dipakai adalah confusion matrix untuk pengecekan hasil prediksi yang dilakukan.

## Data Understanding
Kumpulan data ini terdiri dari data penempatan mahasiswa di kampus XYZ. Ini termasuk persentase dan spesialisasi sekolah menengah dan sekolah menengah atas. Ini juga mencakup spesialisasi gelar, jenis dan Pengalaman kerja dan penawaran gaji kepada siswa yang ditempatkan<br> 

Dataset: [Campus Recruitment](https://www.kaggle.com/datasets/benroshan/factors-affecting-campus-placement).  

### Variabel-variabel pada Heart Failure Prediction Dataset adalah sebagai berikut:
- gender = Jenis Kelamin Mahasiswa ['Laki-Laki', 'Perempuan']
- hsc_b = Dewan Pendidikan Mahasiswa ['Central', 'Others']
- hsc_s = Peminatan dalam Pendidikan Menengah Atas ['Commerce', 'Science', 'Arts']
- degree_t = Kelulusan (Jenis gelar) - Bidang pendidikan gelar ['Sci&Tech', 'Comm&Mgmt', 'Others'])
- workex = Pengalaman Kerja ['No', 'Yes'])
- salary = Gaji yang ditawarkan oleh perusahaan kepada kandidat ['rendah', 'sedang', 'tinggi']
- specialisation = Pasca Sarjana (MBA) - Spesialisasi ['Mkt&HR', 'Mkt&Fin']
- ssc_p = Persentase Pendidikan Menengah - Kelas 10
- hsc_p = Persentase Pendidikan Menengah Atas- Kelas 12
- degree_p = Persentase Gelar
- etest_p = Persentase tes kemampuan kerja (dilakukan oleh perguruan tinggi)
- mba_p = Persentase MBA

berdasarkan penjelasan fitur diatas, terdapat 2 tipe data yaitu numeric (int dan float) dan object. tipe data object ditunjukan dengan atribut yang memiliki kategori:

<img width="221" alt="image" src="https://github.com/mzidanhusaini/knn_campus_rec/assets/149399304/8ec41480-e020-47ae-a47b-0919d05f81ea">

selanjutnya pengecekan apakah terdapat dataset yang kosong atau tidak:
```
df.isnull().sum()
```

<img width="106" alt="image" src="https://github.com/mzidanhusaini/knn_campus_rec/assets/149399304/668ded4a-6c67-49e0-8b19-7da092e9303e">

terdapat data yang kosong pada atribut salary (gaji)

## EDA
1. jumlah gender dalam dataset:

![image](https://github.com/mzidanhusaini/knn_campus_rec/assets/149399304/0fe1fe8c-7a7c-4213-9cb9-d7da5a1910a1)

Jenis kelamin Laki-laki memiliki jumlah yang lebih banyak dari pada perempuan

2. Penyebaran status penerimaan:

![image](https://github.com/mzidanhusaini/knn_campus_rec/assets/149399304/76209436-4490-423f-b08b-cbdcccf236b5)

didalam dataset tersebut terdapat 68,8% mahasiswa yang termasuk kedalam kategori placed atau di terima sedangkan hanya 31,2% mahasiswa yang tidak lolos.

3. Jumlah dewan pendidikan mahasiswa:

![image](https://github.com/mzidanhusaini/knn_campus_rec/assets/149399304/b1eca09d-d709-4a13-9827-f0f3cb7a211a)

dewan pendidikan yang dimiliki kebanyakan dari mahasiswa dalam dataset tersebut adalah Central.

4. Jumlah peminatan dalam pendidikan menengan tinggi dalam dataset:
![image](https://github.com/mzidanhusaini/knn_campus_rec/assets/149399304/7237c3db-e65e-41aa-9f65-2194060d5e2d)

peminatan tertinggi didalam dataset adalah commerce (bisnis).

5. Jenis gelar:

![image](https://github.com/mzidanhusaini/knn_campus_rec/assets/149399304/0edce460-6dc4-437a-ba98-d788b5f78ea3)

jenis gelar yang didapatkan mahasiswa ketika lulus adalah Comm&Mgmt (mahasiswa jurusan bisnis)

7. hasil penerimaan berdasarkan jenis kelamin:

![image](https://github.com/mzidanhusaini/knn_campus_rec/assets/149399304/f110085c-e3bf-4752-9200-769ded870498)

![image](https://github.com/mzidanhusaini/knn_campus_rec/assets/149399304/4c55d142-30fa-4a88-b2e4-f879fb096bb1)

berdasarkan dua visualisasi tersebut dapat disimpulkan jika laki-laki yang lulus lebih banyak dibandingkan dengan perempuan dan jumlah perempuan yang tidak lulus lebih sedikit dibandingkan dengan laki-laki.

8. tingkat kelulusan berdasarkan jurusan

![image](https://github.com/mzidanhusaini/knn_campus_rec/assets/149399304/0586434b-cf3d-4854-ac9d-5080faada3ad)

Jurusan bisnis memiliki tingkat kelulusan yang lebih tinggi dibandingkan dengan jurusan lainnya, lalu disusul oleh jurusan keilmuan sains dan seni.

9. distribusi gaji yang di tawarkan:

![image](https://github.com/mzidanhusaini/knn_campus_rec/assets/149399304/ee158ec0-56f0-4214-a5e3-7fd206c3b725)

range gaji yang ditawarkan perusahaan ada pada range 200 - 400 ribu.

## Data Preparation
tahap pertama yang dilakukan adalah menghapus atribut yang tidak akan dipakai dikarenakan memiliki isi data dan penjelasan fitur yang sama dengan fitur lainnya:
```
df = df.drop(['sl_no','ssc_b'],axis=1)
```

dikarenakan terdapat data yang kosong dan setelah di analisis kembali data tersebut tidak bisa dihapus maka data tersebut diisi dengan angka 0:
```
df['salary'] = df['salary'].fillna(0)
```

selanjutnya merubah fitur gaji menjadi range rendah, sedang dan tinggi:


## Modeling
Tahapan ini membahas mengenai model machine learning yang digunakan untuk menyelesaikan permasalahan. Anda perlu menjelaskan tahapan dan parameter yang digunakan pada proses pemodelan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan kelebihan dan kekurangan dari setiap algoritma yang digunakan.
- Jika menggunakan satu algoritma pada solution statement, lakukan proses improvement terhadap model dengan hyperparameter tuning. **Jelaskan proses improvement yang dilakukan**.
- Jika menggunakan dua atau lebih algoritma pada solution statement, maka pilih model terbaik sebagai solusi. **Jelaskan mengapa memilih model tersebut sebagai model terbaik**.

## Evaluation
Pada bagian ini anda perlu menyebutkan metrik evaluasi yang digunakan. Lalu anda perlu menjelaskan hasil proyek berdasarkan metrik evaluasi yang digunakan.

Sebagai contoh, Anda memiih kasus klasifikasi dan menggunakan metrik **akurasi, precision, recall, dan F1 score**. Jelaskan mengenai beberapa hal berikut:
- Penjelasan mengenai metrik yang digunakan
- Menjelaskan hasil proyek berdasarkan metrik evaluasi

Ingatlah, metrik evaluasi yang digunakan harus sesuai dengan konteks data, problem statement, dan solusi yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan formula metrik dan bagaimana metrik tersebut bekerja.

## Deployment
pada bagian ini anda memberikan link project yang diupload melalui streamlit share. boleh ditambahkan screen shoot halaman webnya.

**---Ini adalah bagian akhir laporan---**

_Catatan:_
- _Anda dapat menambahkan gambar, kode, atau tabel ke dalam laporan jika diperlukan. Temukan caranya pada contoh dokumen markdown di situs editor [Dillinger](https://dillinger.io/), [Github Guides: Mastering markdown](https://guides.github.com/features/mastering-markdown/), atau sumber lain di internet. Semangat!_
- Jika terdapat penjelasan yang harus menyertakan code snippet, tuliskan dengan sewajarnya. Tidak perlu menuliskan keseluruhan kode project, cukup bagian yang ingin dijelaskan saja.


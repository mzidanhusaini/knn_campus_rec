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

```
df['salary'] = pd.cut(df['salary'], bins=[0, 300000, 600000, 940000], labels=['rendah', 'sedang', 'tinggi'])
```
dikarenakan setelah rubah menjadi kategori terdapat dataset yang Null lagi maka dilakukan proses pengisian data yang null dengan rendah, dikarenakan nilai pada fitur gaji adalah 0:

```
df['salary'].fillna('rendah', inplace=True)
```

selanjutnya adalah pembagian fitur numeric dan kategori:

```
numerical = []
catgcol = []

for col in df.columns:
  if df[col].dtype=='float64':
    numerical.append(col)
  else:
    catgcol.append(col)

for col in df.columns:
  if col in numerical:
    df[col].fillna(df[col].median(), inplace=True)
  else:
    df[col].fillna(df[col].mode()[0], inplace=True)
```
setelah dipisahkan data kategori dan numeric, mari kita transform data tersebut menjadi numeric dengan library LabelEncoder:

```
le = LabelEncoder()

for col in catgcol:
  df[col] = le.fit_transform(df[col])
```

dataset siap untuk dilanjut ke tahap modeling.

## Modeling
1. menentukan nilai X dan Y:
```
X = df.drop("status",axis = 1)
y = df.status
```
2. pembagian data train dan test:
```
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=0)
```
3. model fitting
```
test_scores = []
train_scores = []

for i in range(1,15):

    knn = KNeighborsClassifier(i)
    knn.fit(X_train,y_train)

    train_scores.append(knn.score(X_train,y_train))
    test_scores.append(knn.score(X_test,y_test))
```
4. cek akurasi data training:
```
max_train_score = max(train_scores)
train_scores_ind = [i for i, v in enumerate(train_scores) if v == max_train_score]
print('Max train score {} % and k = {}'.format(max_train_score*100,list(map(lambda x: x+1, train_scores_ind))))
```
<img width="181" alt="image" src="https://github.com/mzidanhusaini/knn_campus_rec/assets/149399304/041c7e13-ab20-4f8c-8a16-fadc01f1e21d">

max akurasi dari data training adalah 100% dengan nilai k = 1

5. cek akurasi testing:
```
max_test_score = max(test_scores)
test_scores_ind = [i for i, v in enumerate(test_scores) if v == max_test_score]
print('Max test score {} % and k = {}'.format(max_test_score*100,list(map(lambda x: x+1, test_scores_ind))))
```
<img width="256" alt="image" src="https://github.com/mzidanhusaini/knn_campus_rec/assets/149399304/84a6d2b9-c78b-4b6b-b1c5-ef6b2f75ea3f">

akurasi dari data testing adalah 80% dengan nilai k = [7, 9, 10, 11, 13, 14]

6. fitting model dengan menentukan nilai k sesuai dengan rekomendasi dari data testing sebelumnya (7):
```
knn = KNeighborsClassifier(7)

knn.fit(X_train,y_train)
knn.score(X_test,y_test)
```

## Evaluation
setelah model dibuat dilakukan tahap evaluasi pengujian model dengan mencoba memasukan data didalam dataset untuk pengecekan hasil apakah sudah sesuai atau belum:
```
input_data = (1,67.00,91.00,1,1,58.00,2,0,55.0,1,58.80,0)

input_data_as_numpy_array = np.array(input_data)

input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = knn.predict(input_data_reshaped)
print(prediction)

if (prediction[0]==0):
  print('Mahasiswa tidak lolos')
else:
  print('Mahasiswa lolos')
```

```
[1]
Mahasiswa lolos
```

hasil prediksi yang di dapatkan sudah sesuai.

Pada bagian ini metrik evaluasi yang digunakan adalah penggunaan Confusion matrix:
```
y_pred = knn.predict(X_test)

cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
p = sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap="YlGnBu" ,fmt='g')
plt.title('Confusion matrix', y=1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
```

![image](https://github.com/mzidanhusaini/knn_campus_rec/assets/149399304/e394f486-b0cd-42fe-8c8f-3cbbc8e4b64b)

saat dilakukan proses pengujuan kategori tidak lolos, model dapat memprediksi 9 benar dan 3 salah lalu untuk kategori lolos model dapat memprediksi 43 data dengan benar dan 10 salah dengan total data testing sebanyak 65 data (53 kategori lolos dan 11 tidak lolos)

adapun pengecekan untuk classification report sebagai berikut:

<img width="263" alt="image" src="https://github.com/mzidanhusaini/knn_campus_rec/assets/149399304/9d9b814b-7726-40ed-ab7a-9a359b8a4f6c">

model yang dibuat mendapatkan nilai akurasi 80%

## Deployment


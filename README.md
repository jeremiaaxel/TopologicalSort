# Stima_Tucil2
Repositori untuk Tugas Kecil 2 Strategi Algoritma Teknik Informatika ITB 2019\
[Spek](https://informatika.stei.itb.ac.id/~rinaldi.munir/Stmik/2020-2021/Tugas-Kecil-2-(2021).pdf)\
[Laporan](https://docs.google.com/document/d/11fiLzSvk1A2qDVrRx1KDa0rc71nT3Ro1tpRWLva4SxY/edit#heading=h.o9xfu0d75rs9)

## Deskripsi
Aplikasi sederhana penyusun rencana pengambilan kuliah. Penyusunan rencana kuliah diimplementasikan dengan pendekatan _Topological Sorting_.
Suatu mata kuliah bisa saja memiliki _prerequisite_/prasyarat. Untuk mengambil mata kuliah tersebut harus mengambil mata kuliah di prasyarat di semester sebelumnya terlebih dahulu.

## Requirement/Instalasi
1. Python

## Cara Menggunakan Program
### 1. Menggunakan manual
Menjalankan program satu kali dan memasukan nama file secara manual
1. Program dijalankan melalui terminal dengan menjalankan ```python src/main.py``` untuk Windows, OS lain menyesuaikan.
2. Kemudian akan muncul _prompt_ untuk memasukan nama file, masukan nama file berisi daftar mata kuliah.
    - File input berformat ```.txt```
    - Satu file berformat :\
      <kode_kuliah_1>, <kode kuliah prasyarat - 1>, <kode kuliah prasyarat - 2>, <kode kuliah prasyarat - 3>.\
      <kode_kuliah_2>, <kode kuliah prasyarat - 1>, <kode kuliah prasyarat - 2>.\
      <kode_kuliah_3>, <kode kuliah prasyarat - 1>, <kode kuliah prasyarat - 2>, <kode kuliah prasyarat - 3>, <kode kuliah prasyarat - 4>.\
      <kode_kuliah_4>.
3. Program akan berjalan dan memunculkan hasilnya.

### 2. Menggunakan script
Menjalankan program sebanyak test case pada folder `test` secara langsung berurutan.
1. Program dijalankan di terminal dengan menjalankan ``` python runner.py``` untuk Windows, OS lain menyesuaikan. Atau dapat juga dengan menjalankan `runner.py` secara langsung.
2. Program akan berjalan dan menampikan semua hasil dari _test case_ yang ada di folder `test`. Ubah isi folder `test` untuk mengubah hasil.

## Author
NIM/Nama : 13519188/Jeremia Axel
Kelas : 04
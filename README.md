# Lab6
Tugas Praktikum 8 Mata Kuliah Program Komputer dan Praktek (Lab6)
===========================================================================================================

Program ini dirancang untuk mengelola data mahasiswa dalam bentuk sederhana. Program ini memungkinkan pengguna untuk:

1. Menambahkan data mahasiswa baru: Pengguna dapat memasukkan nama dan nilai mahasiswa baru, yang kemudian akan disimpan dalam sebuah list.


2. Menampilkan semua data mahasiswa: Program akan menampilkan daftar lengkap semua mahasiswa yang telah tersimpan, beserta nama dan nilainya.


3. Menghapus data mahasiswa: Pengguna dapat menghapus data mahasiswa tertentu dengan memasukkan nama mahasiswa yang ingin dihapus.


4. Mengubah nilai mahasiswa: Pengguna dapat mengubah nilai mahasiswa tertentu dengan memasukkan nama mahasiswa dan nilai baru.

**Penjelasan Detail:**

    List mahasiswa: 
    List ini digunakan untuk menyimpan data mahasiswa. Setiap elemen dalam list adalah sebuah dictionary yang berisi dua key: 
    'nama' (untuk menyimpan nama mahasiswa) dan 'nilai' (untuk menyimpan nilai mahasiswa).


    Fungsi tambah(): 
    Fungsi ini menambahkan data mahasiswa baru ke dalam list mahasiswa. Pengguna diminta memasukkan nama dan nilai, 
    kemudian data tersebut disimpan dalam bentuk dictionary dan ditambahkan ke list.


    Fungsi tampilkan(): 
    Fungsi ini mencetak semua data mahasiswa yang tersimpan dalam format yang mudah dibaca. 
    
    Jika list mahasiswa kosong, maka akan ditampilkan pesan bahwa data masih kosong.

    Fungsi hapus(nama): 
    Fungsi ini mencari mahasiswa dengan nama yang diberikan. Jika ditemukan, data mahasiswa tersebut akan dihapus dari list. 
    Jika tidak ditemukan, akan ditampilkan pesan bahwa data tidak ditemukan.


    Fungsi ubah(nama): 
    Fungsi ini mencari mahasiswa dengan nama yang diberikan. Jika ditemukan, pengguna akan diminta memasukkan nilai baru, dan nilai lama akan diganti dengan nilai baru. 
    Jika tidak ditemukan, akan ditampilkan pesan bahwa data tidak ditemukan.


    Loop Utama: 
    Loop while True menjalankan program secara berulang hingga pengguna memilih untuk keluar. Pada setiap iterasi, 
    program menampilkan menu pilihan dan meminta pengguna untuk memilih tindakan yang ingin dilakukan.


**Flowchart**
![Flowchart lab 6](https://github.com/user-attachments/assets/0926f5a1-2c69-4e22-ab5c-a28f6c0d1a9a)


**Kode Program**
![koding lab6](https://github.com/user-attachments/assets/deac408d-ff9c-4dc0-a6bf-239b655657ac)
![koding lab6 2](https://github.com/user-attachments/assets/609f20d9-6da6-497b-a4c5-ed7bfa825cc1)



**Hasil Program**
![Hasil Lab 6](https://github.com/user-attachments/assets/3bea321e-207b-4db9-a65d-2b7788b34a9a)

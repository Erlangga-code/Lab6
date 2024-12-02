mahasiswa = []

def tambah():
  nama = input("Masukkan nama mahasiswa: ")
  nilai = int(input("Masukkan nilai: "))
  mahasiswa.append({"nama": nama, "nilai": nilai})
  print("Data mahasiswa berhasil ditambahkan!")

def tampilkan():
  if len(mahasiswa) == 0:
    print("Data mahasiswa masih kosong.")
  else:
    print("Daftar Mahasiswa:")
    for mhs in mahasiswa:
      print(f"Nama: {mhs['nama']}, Nilai: {mhs['nilai']}")

def hapus(nama):
  for i, mhs in enumerate(mahasiswa):
    if mhs['nama'] == nama:
      del mahasiswa[i]
      print(f"Data mahasiswa dengan nama {nama} berhasil dihapus.")
      return
  print(f"Data mahasiswa dengan nama {nama} tidak ditemukan.")

def ubah(nama):
  for i, mhs in enumerate(mahasiswa):
    if mhs['nama'] == nama:
      nilai_baru = int(input("Masukkan nilai baru: "))
      mahasiswa[i]['nilai'] = nilai_baru
      print(f"Data mahasiswa dengan nama {nama} berhasil diubah.")
      return
  print(f"Data mahasiswa dengan nama {nama} tidak ditemukan.")

while True:
  print("\nMenu:")
  print("1. Tambah data")
  print("2. Tampilkan data")
  print("3. Hapus data")
  print("4. Ubah data")
  print("5. Keluar")

  pilihan = input("Pilih menu: ")

  if pilihan == '1':
    tambah()
  elif pilihan == '2':
    tampilkan()
  elif pilihan == '3':
    nama = input("Masukkan nama mahasiswa yang akan dihapus: ")
    hapus(nama)
  elif pilihan == '4':
    nama = input("Masukkan nama mahasiswa yang akan diubah: ")
    ubah(nama)
  elif pilihan == '5':
    break
  else:
    print("Pilihan tidak valid.")

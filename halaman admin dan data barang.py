class Barang:
    def __init__(self, id_barang, nama_barang, harga_barang, stok_barang):
        self.id_barang = id_barang
        self.nama_barang = nama_barang
        self.harga_barang = harga_barang
        self.stok_barang = stok_barang

# Data awal barang
daftar_barang = [
    Barang(1, "Semen", 10000, 50),
    Barang(2, "Batako", 5000, 100),
    Barang(3, "Gergaji", 40000, 40),
    Barang(4, "Palu", 25000, 30),
]

# Fungsi untuk menampilkan daftar barang
def tampilkan_daftar_barang():
    print("=== DAFTAR BARANG ===")
    for barang in daftar_barang:
        print(f"ID Barang: {barang.id_barang}")
        print(f"Nama Barang: {barang.nama_barang}")
        print(f"Harga Barang: {barang.harga_barang}")
        print(f"Stok Barang: {barang.stok_barang}")
        print("------------------------")

# Fungsi untuk menambahkan barang baru
def tambah_barang():
    id_barang = int(input("Masukkan ID Barang: "))
    nama_barang = input("Masukkan Nama Barang: ")
    harga_barang = int(input("Masukkan Harga Barang: "))
    stok_barang = int(input("Masukkan Stok Barang: "))
    barang_baru = Barang(id_barang, nama_barang, harga_barang, stok_barang)
    daftar_barang.append(barang_baru)
    print("Barang telah ditambahkan!")

# Fungsi untuk mengubah data barang
def ubah_barang():
    id_barang = int(input("Masukkan ID Barang yang akan diubah: "))
    for Barang in daftar_barang:
        if Barang.id_barang == id_barang:
            new_stok_barang = int(input("Masukkan Stok Barang yang baru: "))
            Barang.stok_barang = new_stok_barang
            print("Data barang telah diubah!")
            return

    print("Barang dengan ID tersebut tidak ditemukan.")

# Fungsi untuk menghapus data barang
def hapus_barang():
    id_barang = int(input("Masukkan ID Barang yang akan dihapus: "))

    # Menghapus barang dari list daftar_barang
    for barang in daftar_barang:
        if barang.id_barang == id_barang:
            daftar_barang.remove(barang)
            print("Data barang telah dihapus!")
            return

    print("Barang dengan ID tersebut tidak ditemukan.")

# Fungsi untuk menampilkan menu Data Barang
def menu_data_barang():
    while True:
        print("=== MENU DATA BARANG ===")
        print("1. Tampilkan Daftar Barang")
        print("2. Tambah Barang")
        print("3. Ubah Data Barang")
        print("4. Hapus Data Barang")
        print("5. Keluar ke Halaman Dashboard Admin")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan_daftar_barang()
        elif pilihan == "2":
            tambah_barang()
        elif pilihan == "3":
            ubah_barang()
        elif pilihan == "4":
            hapus_barang()
        elif pilihan == "5":
            break
        else:
            print("Menu tidak valid")

# Fungsi untuk menampilkan Halaman Admin
def halaman_admin():
    print("=== HALAMAN ADMIN ===")
    print("Selamat datang di Halaman Admin")
    while True:
        print("Silakan pilih menu yang tersedia:")
        print("1. Data Barang")
        print("2. Riwayat Penjualan")
        print("3. Pengaturan Toko")
        print("4. Bantuan")
        print("5. Tentang Aplikasi")
        print("6. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            menu_data_barang()
        elif pilihan == "2":
            # Tampilkan riwayat penjualan
            pass
        elif pilihan == "3":
            # Tampilkan menu pengaturan toko
            pass
        elif pilihan == "4":
            # Tampilkan menu bantuan
            pass
        elif pilihan == "5":
            # Tampilkan tentang aplikasi
            pass
        elif pilihan == "6":
            # Keluar program
            break
        else:
            print("Menu tidak valid")

# Menampilkan Halaman Admin
halaman_admin()







import textwrap

class Barang:
    def __init__(self, id_barang, nama_barang, harga_barang, stok_barang):
        self.id_barang = id_barang
        self.nama_barang = nama_barang
        self.harga_barang = harga_barang
        self.stok_barang = stok_barang

class Toko:
    def __init__(self):
        self.metode_pembayaran = ["Cash", "Transfer"]
        self.array_metode_pengiriman = ["JNE", "Tiki"]
        self.data_toko = {"nama_toko": "", "alamat_toko": "", "nomor_telepon": ""}

    def atur_informasi_toko(self):
        print("+----------+++---------+")
        print("|  ATUR INFORMASI TOKO |")
        print("+----------+++---------+")
        self.data_toko.update({
            "nama_toko": input("Masukkan Nama Toko: "),
            "alamat_toko": input("Masukkan Alamat Toko: "),
            "nomor_telepon": input("Masukkan Nomor Telepon Toko: "),
        })
        print("Informasi toko berhasil diatur.")

    def tambah_metode_pembayaran(self):
        print("+----------+++---------+")
        print("|ATUR METODE PEMBAYARAN|")
        print("+----------+++---------+")
        metode_baru = input("Masukkan Metode Pembayaran Baru: ")
        self.metode_pembayaran.append(metode_baru)
        print(f"Metode pembayaran '{metode_baru}' berhasil ditambahkan.")

    def tambah_metode_pengiriman(self):
        print("+----------+++---------+")
        print("|ATUR METODE PENGIRIMAN|")
        print("+----------+++---------+")
        metode_pengiriman_baru = input("Masukkan Metode Pengiriman Baru: ")
        self.array_metode_pengiriman.append(metode_pengiriman_baru)
        print(f"Metode pengiriman '{metode_pengiriman_baru}' berhasil ditambahkan.")

    def tampilkan_informasi_toko(self):
        print("+----------+++---------+")
        print("|    INFORMASI TOKO    |")
        print("+----------+++---------+")
        for key, value in self.data_toko.items():
            print(f"{key.capitalize()}: {value}")
        print(f"Metode Pembayaran: {', '.join(self.metode_pembayaran)}")
        print(f"Metode Pengiriman: {', '.join(self.array_metode_pengiriman)}")

    def tampilkan_menu_pengaturan_toko(self):
        while True:
            print("+----------+++---------+")
            print("| MENU PENGATURAN TOKO |")
            print("+----------+++---------+")
            print("1. Atur Informasi Toko")
            print("2. Metode Pembayaran")
            print("3. Metode Pengiriman")
            print("4. Tampilkan Informasi Toko")
            print("5. Kembali ke Halaman Admin")

            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                self.atur_informasi_toko()
            elif pilihan == "2":
                self.tambah_metode_pembayaran()
            elif pilihan == "3":
                self.tambah_metode_pengiriman()
            elif pilihan == "4":
                self.tampilkan_informasi_toko()
            elif pilihan == "5":
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

class TentangAplikasi:
    def menu_tentang_aplikasi(self):
        print("+----------+++---------+")
        print("|   TENTANG APLIKASI   |")
        print("+----------+++---------+")
        print("Program Kasir ini digunakan untuk mempermudah manajemen toko bangunan BBC! :)")
        print("Program ini dibuat untuk tugas proyek akhir Praktikum Pemrograman Komputer")
        print("Aplikasi ini dapat diunduh pada www.bbcdownload.com")
        print("Dibuat oleh :")
        print("1. Gigha Bekti Prakoso")
        print("2. Arista Ilyatus Septiya Putri")
        print("3. Nayla Kamalati Putri")
        print("4. Aini Intan Cahyani")
        print("\nTerima kasih telah menggunakan aplikasi ini")

        print("versi 3.5")

class HalamanAdmin:
    def __init__(self):
        self.toko = Toko()
        self.tentang_aplikasi = TentangAplikasi()
        self.daftar_barang = [
            Barang(1, "Semen", 10000, 50),
            Barang(2, "Batako", 5000, 100),
            Barang(3, "Gergaji", 40000, 40),
            Barang(4, "Palu", 25000, 30),
        ]
        self.riwayat_penjualan = []

    
    def catat_transaksi(self, id_barang, jumlah, metode_pembayaran):
        for barang in self.daftar_barang:
            if barang.id_barang == id_barang:
                if jumlah <= barang.stok_barang:
                    # Kurangi stok barang
                    barang.stok_barang -= jumlah

                    # Catat transaksi
                    waktu_transaksi = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    total_harga = jumlah * barang.harga_barang
                    transaksi = {
                        "id_barang": id_barang,
                        
  
"nama_barang": barang.nama_barang,
                        "jumlah": jumlah,
                        "total_harga": total_harga,
                        "waktu_transaksi": waktu_transaksi,
                        "metode_pembayaran": metode_pembayaran
                    }
                    self.riwayat_penjualan.append(transaksi)
                    print("Transaksi berhasil dicatat")
                    return

        print("Barang dengan ID tersebut tidak ditemukan atau stok tidak mencukupi")

    def tampilkan_daftar_barang(self):
        print("+----------+++---------+")
        print("|     DAFTAR BARANG    |")
        print("+----------+++---------+")
        print("+" + "-"*7 + "+" + "-"*102 + "+" + "-"*12 + "+" + "-"*12 + "+")
        print("|" + "ID".center(5) + "|" + "Nama".center(100) + "|" +  
              "Harga".center(10) + "|" + "Stok".center(10) + "|")
        print("+" + "-"*7 + "+" + "-"*102 + "+" + "-"*12 + "+" + "-"*12 + "+")
    
        for barang in self.daftar_barang:
            wrapped_name = textwrap.fill(barang.nama_barang, width=100)
            print("|" + str(barang.id_barang).center(5) + "|" +  
                  wrapped_name.center(100) + "|" +  
                  str(barang.harga_barang).center(10) + "|" +
                  str(barang.stok_barang).center(10) + "|")
              
        print("+" + "-"*7 + "+" + "-"*102 + "+" + "-"*12 + "+" + "-"*12 + "+")

    def tambah_barang(self):
        print("Tambah Barang")
        id_barang = int(input("Masukkan ID barang: "))
        nama_barang = input("Masukkan nama barang: ")
        harga_barang = int(input("Masukkan harga barang: "))
        stok_barang = int(input("Masukkan stok barang: "))

        barang_baru = Barang(id_barang, nama_barang, harga_barang, stok_barang)

        self.daftar_barang.append(barang_baru)

        print("Barang berhasil ditambahkan")
        self.tampilkan_daftar_barang()
        
    def ubah_barang(self):
        id_barang = int(input("Masukkan ID Barang yang akan diubah: "))
        for barang in self.daftar_barang:
            if barang.id_barang == id_barang:
                print("1. Ubah Nama Barang")
                print("2. Ubah Harga Barang")
                print("3. Ubah Stok Barang")
                pilihan = input("Pilihan edit (1-3): ")
                if pilihan == "1":
                    new_nama = input("Masukkan Nama Barang yang baru: ")
                    barang.nama_barang = new_nama
                    print("Nama Barang telah diubah!")
                elif pilihan == "2":
                    new_harga = int(input("Masukkan Harga Barang yang baru: "))
                    barang.harga_barang = new_harga
                    print("Harga Barang telah diubah!")
                elif pilihan == "3":
                    new_stok = int(input("Masukkan Stok Barang yang baru: "))
                    barang.stok_barang = new_stok
                    print("Stok Barang telah diubah!")
                else:
                    print("Pilihan tidak valid!")
                return

        print("Barang dengan ID tersebut tidak ditemukan.")

    def hapus_barang(self):
        id_barang = int(input("Masukkan ID barang yang ingin dihapus: "))

        for i in range(len(self.daftar_barang)):
            if id_barang == self.daftar_barang[i].id_barang:
                del self.daftar_barang[i]
                break

        print("Data barang berhasil dihapus")
        self.tampilkan_daftar_barang()
        
    def tampilkan_riwayat_penjualan(self):
        print("+----------+++---------+")
        print("|   RIWAYAT PENJUALAN  |")
        print("+----------+++---------+")
        if not self.riwayat_penjualan:
            print("Belum ada riwayat penjualan")
            return

        for transaksi in self.riwayat_penjualan:
            print(f"Waktu Transaksi: {transaksi['waktu_transaksi']}")
            print(f"ID Barang: {transaksi['id_barang']}")
            print(f"Nama Barang: {transaksi['nama_barang']}")
            print(f"Jumlah: {transaksi['jumlah']}")
            print(f"Total Harga: {transaksi['total_harga']}")
            print(f"Metode Pembayaran: {transaksi['metode_pembayaran']}")
            print("=" * 40)
        

    def menu_data_barang(self):
        while True:
            print("+----------+++---------+")
            print("|    MENU DATA BARANG  |")
            print("+----------+++---------+")
            print("1. Tampilkan Daftar Barang")
            print("2. Tambah Barang")
            print("3. Ubah Data Barang")
            print("4. Hapus Data Barang")
            print("5. Kembali ke Halaman Admin")

            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                self.tampilkan_daftar_barang()
            elif pilihan == "2":
                self.tambah_barang()
            elif pilihan == "3":
                self.ubah_barang()
            elif pilihan == "4":
                self.hapus_barang()
            elif pilihan == "5":
                break
            else:
                print("Menu tidak valid")

    def menu_bantuan(self):
        print("+----------+++---------+")
        print("|      MENU BANTUAN    |")
        print("+----------+++---------+")
        print("1. Halaman Admin:")
        print("   - Halaman ini memungkinkan Anda mengakses berbagai fitur administratif.")
        print("   - Anda dapat mengelola data barang, transaksi, riwayat penjualan, dan lainnya.")
        print("\n2. Data Barang:")
        print("   - Pada halaman ini, Anda dapat melihat, menambah, mengubah, dan menghapus data barang.")
        print("   - Setiap barang memiliki ID, nama, harga, dan stok.")
        print("\n3. Pengaturan:")
        print("   - Halaman ini memungkinkan Anda melakukan pengaturan terhadap informasi toko.")
        print("   - Nama Toko, Alamat, Kontak dan Metode Pengiriman dapat diubah oleh Admin.")
        print("\n4. Riwayat Penjualan:")
        print("   - Riwayat penjualan mencatat transaksi yang telah dilakukan.")
        print("   - Anda dapat melihat detail transaksi termasuk barang yang dibeli dan total harga.")
        print("\nTerima kasih telah menggunakan sistem admin. Jika ada pertanyaan lebih lanjut silakan hubungi tim dukungan.")



    def halaman_admin(self):
        while True:
            print("+--------------------------------------+")
            print("|            DASHBOARD ADMIN           |")
            print("+--------------------------------------+")
            print("Selamat datang di Halaman Admin")
            print("Silakan pilih menu yang tersedia:")
            print("1. Data Barang")
            print("2. Riwayat Penjualan")
            print("3. Pengaturan Toko")
            print("4. Bantuan")
            print("5. Tentang Aplikasi")
            print("6. Keluar")

            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                self.menu_data_barang()
            elif pilihan == "2":
                self.tampilkan_riwayat_penjualan()
            elif pilihan == "3":
                self.toko.tampilkan_menu_pengaturan_toko()
            elif pilihan == "4":
                self.menu_bantuan()
            elif pilihan == "5":
                self.tentang_aplikasi.menu_tentang_aplikasi()
                pass
            elif pilihan == "6":
                # Keluar program
                break
            else:
                print("Menu tidak valid")

# Membuat objek dan menjalankan program
admin_page = HalamanAdmin()
admin_page.halaman_admin()





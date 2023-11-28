class Barang:
    def __init__(self, id_barang, nama, harga, stok):
        self.id_barang = id_barang
        self.nama = nama
        self.harga = harga
        self.stok = stok

class TokoBangunan:
    def __init__(self):
        self.profil = {}
        self.daftar_barang = [
            Barang(1, "Semen", 10000, 50),
            Barang(2, "Batako", 5000, 100),
            Barang(3, "Gergaji", 40000, 40),
            Barang(4, "Palu", 25000, 30),
            # Isi daftar_barang dengan barang-barang yang Anda punya
        ]
        self.shopping_cart = {}
        self.riwayat_penjualan = [] 
    
    def tampilkan_produk(self):
        print("+--------------------------------------------+")
        print("|                DAFTAR PRODUK               |")
        print("+----+-------------------+------------+------|")
        print("| ID |     Nama Barang   |   Harga    | Stok |")
        print("+----+-------------------+------------+------|")
        for barang in self.daftar_barang:
            print(f"| {barang.id_barang:<3} | {barang.nama:<17} | {barang.harga:>10} | {barang.stok:>3} |")
        print("+----+-------------------+------------+------|")
       
        
    def beli_barang(self):
        while True:
            self.tampilkan_produk()
            id_barang = input("\nMasukkan ID barang yang ingin dibeli (atau ketik 'x' untuk apabila berhenti menambahkan): ")

            if id_barang.lower() == 'x':
                break

            # Validasi ID barang
            id_barang = int(id_barang)
            barang_ditemukan = False
            for barang in self.daftar_barang:
                if barang.id_barang == id_barang:
                    barang_ditemukan = True
                    jumlah_beli = int(input("Masukkan jumlah yang ingin dibeli: "))

                    if jumlah_beli > barang.stok:
                        print("Maaf, stok tidak mencukupi.")
                    else:
                        if barang.nama in self.shopping_cart:
                            self.shopping_cart[barang.nama] += jumlah_beli
                        else:
                            self.shopping_cart[barang.nama] = jumlah_beli

                        barang.stok -= jumlah_beli
                        print(f"Barang {barang.nama} sebanyak {jumlah_beli} berhasil ditambahkan ke keranjang.")

            if not barang_ditemukan:
                print("ID barang tidak valid. Silakan coba lagi.")

        edit_pesanan = input("Apakah Anda ingin mengedit pesanan? (y/n): ")
        if edit_pesanan.lower() == 'y':
            id_barang_edit = int(input("Masukkan ID barang yang ingin diedit: "))
            for nama_barang, jumlah in self.shopping_cart.items():
                for barang in self.daftar_barang:
                    if barang.id_barang == id_barang_edit:
                        jumlah_baru = int(input("Masukkan jumlah baru: "))
                        if jumlah_baru <= barang.stok:
                            self.shopping_cart[barang.nama] = jumlah_baru
                            barang.stok += jumlah  # Mengembalikan stok yang sebelumnya dibeli
                            print(f"Pesanan berhasil diubah untuk barang {barang.nama}.")
                        else:
                            print("Maaf, stok tidak mencukupi untuk perubahan ini.")
                        break
                else:
                    print("ID barang tidak ditemukan dalam keranjang belanja.")   
                    
    def catat_transaksi(self, shopping_cart, metode_pembayaran):
        for nama_barang, jumlah in shopping_cart.items():
            for barang in self.daftar_barang:
                if barang.nama == nama_barang:
                    if jumlah <= barang.stok:
                        # Kurangi stok barang
                        barang.stok -= jumlah

                        # Catat transaksi
                        total_harga = jumlah * barang.harga
                        transaksi = {
                            "id_barang": barang.id_barang,
                            "nama_barang": barang.nama,
                            "jumlah": jumlah,
                            "total_harga": total_harga,
                            "metode_pembayaran": metode_pembayaran
                        }
                        self.riwayat_penjualan.append(transaksi)
                        print("Transaksi berhasil dicatat")
                    else:
                        print(f"Stok {nama_barang} tidak mencukupi untuk transaksi ini.")

    def tampilkan_riwayat(self):
        if not self.riwayat_penjualan:  # Periksa apakah daftar riwayat penjualan kosong
            print("Belum terdapat transaksi.")
        else :
            print("\n+---- RIWAYAT PENJUALAN ----+")
        for idx, transaksi in enumerate(self.riwayat_penjualan, start=1):
            print(f"Transaksi ke-{idx}:")
            print(f"ID Barang: {transaksi['id_barang']}")
            print(f"Nama Barang: {transaksi['nama_barang']}")
            print(f"Jumlah: {transaksi['jumlah']}")
            print(f"Total Harga: {transaksi['total_harga']}")
            print(f"Metode Pembayaran: {transaksi['metode_pembayaran']}")
            print("+--------------------------+")

    def checkout(self):
        print("\nDaftar Belanja Anda:")
        total_harga = 0
        for nama_barang, jumlah in self.shopping_cart.items():
            for barang in self.daftar_barang:
                if barang.nama == nama_barang:
                    subtotal = jumlah * barang.harga
                    total_harga += subtotal
                    print(f"{nama_barang} - {jumlah} pcs - Harga: {subtotal}")

        print(f"\nTotal Belanja Anda: Rp {total_harga}")
        
        beli_lagi = input("Apakah Anda ingin melanjutkan untuk melakukan pembayaran? (y/n): ")
        if beli_lagi.lower() == 'y':
            metode_pembayaran = input("Pilih metode pembayaran (Cash/Transfer): ")
            if metode_pembayaran.lower() == 'cash':
                uang_dibayar = int(input("Masukkan jumlah uang yang dibayarkan: "))
                if uang_dibayar >= total_harga:
                    kembalian = uang_dibayar - total_harga
                    print(f"Terima kasih! Kembalian Anda: Rp {kembalian}")
                    self.catat_transaksi(self.shopping_cart, metode_pembayaran)
                    self.shopping_cart = {}
                else:
                    print("Maaf, uang yang dibayarkan kurang.")
            elif metode_pembayaran.lower() == 'transfer':
                print("Pilihan bank transfer:")
                print("1. Bank BNI")
                print("2. Bank Mandiri")
                print("3. Bank BCA")
                bank = input("Pilih bank (1/2/3): ")
                if bank in ('1', '2', '3'):
                    no_rekening = {
                        '1': '1263749261736',
                        '2': '47269372736',
                        '3': '1928765382'
                    }
                    print(f"Silakan transfer sejumlah Rp {total_harga} ke nomor rekening {no_rekening[bank]}. Tunjukkan bukti transfer kepada pegawai kasir")
                    self.catat_transaksi(self.shopping_cart, f"Transfer - Bank {bank}")
                    self.shopping_cart = {}
                else:
                    print("Pilihan bank tidak valid.")
            else:
                print("Metode pembayaran tidak valid.")
        else:
            print("Pembayaran dibatalkan.")
            self.shopping_cart = {}

    def tampilkan_homepage(self):
        print("+-------------------------------------+")
        print("|          SELAMAT DATANG DI          |")
        print("|           HALAMAN BERANDA           |")
        print("|                                     |")
        print("|          Toko Bangunan BBC          |")
        print("|   Jl. Acasia No. 58, Mlati, Sleman  |")
        print("|             088237281972            |")
        print("+-------------------------------------+")
        print("Menu Utama:")
        print("1. Product Page")
        print("2. Shopping Cart")
        print("3. Checkout")
        print("4. Purchase History")
        print("5. Account Settings")
        print("6. Help and Support")
        print("7. Keluar")

    def tampilkan_faq_dan_bantuan(self):
        print("+---- FAQ dan Bantuan ----+")
        print("Q: Bisakah barang dikembalikan secara bersyarat?")
        print("A: Ya, Barang dapat dikembalikan dalam waktu 7 hari setelah pembelian dengan syarat tertentu.")

        print("\nQ: Bagaimana cara menghubungi layanan pelanggan?")
        print("A: Anda dapat menghubungi kami melalui no telepon: 088237281972.")

        print("\nQ: Bagaimana cara memesan produk?")
        print("A: Anda dapat memesan produk kami melalui aplikasi atau berkunjung langsung ke toko kami.")

    def account_setting(self):
        print("+---- Account Setting ----+")
        print("Masukkan profil pengguna:")
        username = input("Username: ")  # Tambahkan inputan username pengguna
        self.profil["Nama"] = input("Nama: ")
        self.profil["Alamat"] = input("Alamat: ")
        self.profil["Kontak"] = input("Kontak: ")

        new_password = input("Masukkan kata sandi baru: ")
        self.password = new_password
        print("Kata sandi berhasil diubah!")

        print("Akun berhasil diatur!")
        
    def menu_utama(self):
        while True:
            self.tampilkan_homepage()  # Tampilkan hanya jika belum ditampilkan sebelumnya
            pilihan_menu = input("Silakan pilih menu (1-7) :")

            if pilihan_menu == '1':
                self.tampilkan_produk()
            elif pilihan_menu == '2':
                self.beli_barang()
            elif pilihan_menu == '3':
                self.checkout()
            elif pilihan_menu == '4':
                 self.tampilkan_riwayat()
            elif pilihan_menu == '5':
                self.account_setting()
            elif pilihan_menu == '6':
                self.tampilkan_faq_dan_bantuan()
            elif pilihan_menu == '7':
                print("\nTerima Kasih!")
                break
            else:
                print("Pilihan menu tidak valid. Silakan coba lagi.")
                
# Penggunaan program
if __name__ == "__main__":
    toko = TokoBangunan()
    toko.menu_utama()




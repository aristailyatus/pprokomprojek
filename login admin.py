# Program Login Toko
print("Selamat datang di Toko Bangunan X :)")
print("-----------------***----------------")

# Inisialisasi username dan password yang benar
username_benar = "admin"
password_benar = "admin123"

# Inisialisasi jumlah percobaan login
jumlah_percobaan = 0

# Input username dan password
while jumlah_percobaan < 3:
    # Meminta input username dan password dari pengguna
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    # Memeriksa kebenaran username dan password
    if username == username_benar and password == password_benar:
        print("-----------------***----------------")
        print("Login berhasil!")
        print("-----------------***----------------")
        # Menampilkan menu dashboard admin
        print("Menu Dashboard Admin")
        break
    else:
        print("Username atau password salah. Silakan coba lagi.")
        jumlah_percobaan += 1




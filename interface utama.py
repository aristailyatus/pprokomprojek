def menu_utama():
    print("Selamat datang!")
    print("Silakan pilih opsi berikut:")
    print("1. Login sebagai Admin")
    print("2. Login sebagai Customer")
    pilihan = input("Masukkan pilihan Anda (1/2): ")
    
    if pilihan == "1":
        menu_login_admin()
    elif pilihan == "2":
        menu_login_customer()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        menu_utama()

def menu_login_admin():
    pass 

def menu_login_customer():
    print("Menu Login Customer")
    print("Silakan pilih opsi login berikut:")
    print("1. Masuk sebagai Guest")
    print("2. Masuk sebagai Pengguna")
    print("3. Buat Akun")
    pilihan = input("Masukkan pilihan Anda (1/2/3): ")
    
    if pilihan == "1":
        menu_client()  # langsung ke homepage
    elif pilihan == "2":
        menu_login_cust()
    elif pilihan == "3":
        menu_register()
    else:
        print("Pilihan tidak valid")
        menu_login_customer()

def menu_client():
    # Kode untuk menu client homepage
    pass  

def menu_login_cust():
    # Kode untuk menu login pengguna
    pass  

def menu_register():
    # Kode untuk menu membuat akun 
    pass  

menu_utama()


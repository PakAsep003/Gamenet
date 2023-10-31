import csv
import os

def check_account(username, password):
    cek_file = os.path.isfile("user_accounts.csv")

    if not cek_file:
        with open("user_accounts.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["username", "password", "saldo"])
            return False

    with open("user_accounts.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["username"] == username and row["password"] == password:
                return True
    return False

def check_admin_account(admin_username, admin_password):
    admin_cek = os.path.isfile("admin_account.csv")

    if not admin_cek:
        with open("admin_account.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["admin_username", "admin_pass"])
            return False

    with open("admin_account.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["admin_username"] == admin_username and row["admin_pass"] == admin_password:
                return True
    return False

def create_account(username, password):
    with open("user_accounts.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, password, 0])  # Saldo awal diatur ke 0

def main_menu():
    while True:
        print("Menu:")
        print("1. Main")
        print("2. Top up")
        print("3. Cek saldo")
        print("4. Keluar")

        pilihan = input("Pilih menu (1/2/3/4): ")

        if pilihan == "1":
            # Implementasi untuk menu Main
            pass
        elif pilihan == "2":
            # Implementasi untuk menu Top up
            pass
        elif pilihan == "3":
            # Implementasi untuk menu Cek saldo
            pass
        elif pilihan == "4":
            # Keluar dari program
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, 3, atau 4.")

# Program Utama
while True:
    print("Selamat datang di Warnet")
    print("Apakah Anda sudah memiliki akun?")
    print("1. Ya")
    print("2. Belum")
    print("3. Login sebagai Admin")

    pilihan = input("Pilih menu (1/2/3): ")
    os.system("cls")

    if pilihan == "1":
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        if check_account(username, password):
            os.system("cls")
            print("Selamat datang,", username)
            main_menu()
        else:
            print("Akun tidak ditemukan. Silakan coba lagi.")
    elif pilihan == "2":
        username = input("Masukkan username untuk membuat akun: ")
        password = input("Masukkan password: ")

        if check_account(username, password):
            print("Akun sudah ada. Silakan gunakan username dan password lain.")
        else:
            create_account(username, password)
            print("Akun berhasil dibuat.")
            os.system("cls")

        main_menu()
    elif pilihan == "3":
        admin_username = input("Masukkan username admin: ")
        admin_password = input("Masukkan password admin: ")

        if check_admin_account(admin_username, admin_password):
            print("Selamat datang admin")
            # Lanjutkan dengan tindakan yang sesuai untuk admin
        else:
            print("Akun admin tidak ditemukan. Silakan coba lagi.")
    else:
        print("Pilihan tidak valid. Silakan pilih 1 atau 2.")
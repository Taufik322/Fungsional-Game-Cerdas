import random

users = {
    1: {
        "username": "user1",
        "password": "user1",
        "point": 0
    },
    2: {
        "username": "user2",
        "password": "user2",
        "point": 0
    },
    3: {
        "username": "user3",
        "password": "user3",
        "point": 0
    }
}

def quiz():
    print("Ini fungsi kuis")

def suit():
    while True:
        print()
        print(f'{"="*7}Selamat Datang Di Batu, Gunting, Kertas!{"="*7}')
        print("Masukkan Pilihan:")
        print("1. Batu")
        print("2. Gunting")
        print("3. Kertas")

        user_action = input("Pilih: ").lower()
        possible_actions = ["batu", "gunting", "kertas"]
        computer_action = random.choice(possible_actions)

        if user_action in possible_actions:
            print(f"\nKamu memilih {user_action}, Komputer memilih {computer_action}.\n")
            if user_action == computer_action:
                print(f"Kedua pemain memilih {user_action}. Seri!")
            elif user_action == "batu":
                if computer_action == "gunting":
                    print("Batu menghancurikan gunting! Kamu menang!")
                else:
                    print("Kertas menutupi batu! Kamu kalah!.")
            elif user_action == "kertas":
                if computer_action == "batu":
                    print("Kertas menutupi batu! Kamu menang!")
                else:
                    print("Gunting memotong kertas! Kamu kalah!.")
            elif user_action == "gunting":
                if computer_action == "kertas":
                    print("Gunting memotong kertas! Kamu menang!")
                else:
                    print("Batu menghancurkan gunting! Kamu kalah!.")

            play_again = input("Ingin bermain lagi? (y/n): ")
            if play_again.lower() != "y":
                break
        else:
            print("Salah input")

def login():
    print(f'\n{"="*7}PEMINJAMAN dan PEMBELIAN KENDARAAN{"="*7}')
    count = 0
    while count == 0:
        akun = input("Masukkan username : ")
        password = input("Masukkan password : ")

        if akun != "" and password != "":
            password = str(password)
            akun = str(akun)

            for sortir in users:
                if akun in users[sortir]["username"] and password == users[sortir]["password"]:
                    dashboard()
                    break
                elif akun in users[sortir]["username"] or password == users[sortir]["password"]:
                    print("Username/Password salah!\n")
                    login()

        else:
            print("____Data tidak boleh kosong!\n")

def dashboard():
    while True:
        print()
        print(f'{"="*7}Selamat Datang Di Hagi!{"="*7}')
        print("1. Kuis Pengetahuan Umum")
        print("2. Batu, Gunting, Kertas")
        print("3. Logout")
        inputs = input("Pilih: ")
        if inputs == '1':
            quiz()
        elif inputs == '2':
            suit()
        elif inputs == '3':
            login()


login()
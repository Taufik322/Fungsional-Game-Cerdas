
users = {
    1: {
        "username": "user1",
        "password": "user1",
        "isLogin": False,
        "point": 0
    },
    2: {
        "username": "user2",
        "password": "user2",
        "isLogin": False,
        "point": 0
    },
    3: {
        "username": "user3",
        "password": "user3",
        "isLogin": False,
        "point": 0
    }
}

questions = ["1. Berapakah hasil dari 1 + 1?",
             "2. Siapa nama bapak Ajeng?",
             "3. Benar atau Salah... Nama bapak Ajeng adalah Asep",
             "4. Di kota manakah Ajeng dilahirkan?",
             "5. Benar atau Salah... Nama terakhir Ajeng adalah Prameswati"]

answer_choices = ["a)1\nb)2\nc)3\nd)4\n:",
                  "a)Joko Widodo\nb)Soeharto\nc)Donald Trump\nd)Asep\n:",
                  ":",
                  "a)Makasar\nb)Manado\nc)Malang\nd)Magelang\n:",
                  ":"]

correct_choices = [{"b", "2"},
                   {"d", "Asep"},
                   {"benar", "b"},
                   {"a", "Makasar"},
                   {"salah", "s"}]

answers = ["1 + 1 adalah 2",
           "Nama bapak Ajeng adalah Asep",
           "Nama bapak Ajeng adalah Asep",
           "Ajeng lahir di kota Makasar",
           "Nama terakhir Ajeng adalah Prameswari"]


def quiz():
    score = 0
    for question, choices, correct_choice, answer in zip(questions, answer_choices, correct_choices, answers):
        print(question)
        user_answer = input(choices).lower()
        if user_answer in correct_choice:
            print("Jawaban Benar!")
            score += 1
            for sortir in users:
                if users[sortir]["isLogin"] == True:
                    users[sortir]["point"] += 10
                    continue
        else:
            print("Jawaban Salah!,", answer)
    print(score, "out of", len(questions), "that is", float(score / len(questions)) * 100, "%")

def suit():
    print("Ini fungsi suit")

def login():
    print(f'\n{"="*7}PEMINJAMAN dan PEMBELIAN KENDARAAN{"="*7}')
    while True:
        akun = input("Masukkan username : ")
        password = input("Masukkan password : ")

        if akun != "" and password != "":
            password = str(password)
            akun = str(akun)

            for sortir in users:
                if akun in users[sortir]["username"] and password == users[sortir]["password"]:
                    users[sortir]["isLogin"] = True
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
        elif inputs == '4':
            print(users)


login()
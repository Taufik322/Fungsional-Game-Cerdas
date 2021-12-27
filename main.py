from operator import getitem
import random

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
             "2. Apa nama ibu kota Indonesia?",
             "3. Benar atau Salah... Mata uang negara Indonesia adalah rupiah",
             "4. Siapa nama presiden pertama negara Indonesia?",
             "5. Benar atau Salah... Bahasa pemrograman Python memerlukan titik koma"]

answer_choices = ["a)1\nb)2\nc)3\nd)4\n:",
                  "a)Malang\nb)Jakarta\nc)Penajam\nd)Bandung\n:",
                  ":",
                  "a)Joko Widodo\nb)Soekarno\nc)Soeharto\nd)Megawati\n:",
                  ":"]

correct_choices = [{"b", "2"},
                   {"c", "Penajam"},
                   {"benar", "b"},
                   {"b", "Soekarno"},
                   {"salah", "s"}]

answers = ["1 + 1 adalah 2",
           "Nama ibu kota Indonesia adalah Penajam",
           "Mata uang negara Indonesia adalah rupiah",
           "Nama presiden pertaman negara Indonesia adalah Soekarno",
           "Bahasa pemrograman Python tidak memerlukan titik koma"]

def plusScore():
    for sortir in users:
        if users[sortir]["isLogin"] == True:
            users[sortir]["point"] += 10
            continue

def quiz():
    score = 0
    for question, choices, correct_choice, answer in zip(questions, answer_choices, correct_choices, answers):
        print(question)
        user_answer = input(choices).lower()
        if user_answer in correct_choice:
            print("Jawaban Benar!")
            score += 1
            plusScore()
        else:
            print("Jawaban Salah!,", answer)
    print(score, "out of", len(questions), "that is", float(score / len(questions)) * 100, "%")

def suit():
    while True:
        print()
        print(f'{"="*7}Selamat Datang Di Batu, Gunting, Kertas!{"="*7}')
        print("Pilih Salah Satu (Batu, Gunting, Kertas")

        user_action = input("Pilih: ").lower()
        possible_actions = ["batu", "gunting", "kertas"]
        computer_action = random.choice(possible_actions)

        if user_action in possible_actions:
            print(f"\nKamu memilih {user_action}, Komputer memilih {computer_action}.\n")
            if user_action == computer_action:
                print(f"Kedua pemain memilih {user_action}. Seri!")
            elif user_action == "batu":
                if computer_action == "gunting":
                    print("Batu menghancurkan gunting! Kamu menang!")
                    plusScore()
                else:
                    print("Kertas menutupi batu! Kamu kalah!.")
            elif user_action == "kertas":
                if computer_action == "batu":
                    print("Kertas menutupi batu! Kamu menang!")
                    plusScore()
                else:
                    print("Gunting memotong kertas! Kamu kalah!.")
            elif user_action == "gunting":
                if computer_action == "kertas":
                    print("Gunting memotong kertas! Kamu menang!")
                    plusScore()
                else:
                    print("Batu menghancurkan gunting! Kamu kalah!.")

            play_again = input("Ingin bermain lagi? (y/n): ")
            if play_again.lower() != "y":
                break
        else:
            print("Salah input")


def hangman():
    print("Selamat datang di game Hangman!")
    list_kata = [
        'api',
        'tas',
        'soto',
        'gula',
        'hujan',
        'motor',
        'mobil',
        'bohong',
        'coklat',
        'lelah',
        'bangsawan',
        'gubuk',
        'pasar',
        'dermawan',
        'pramugara',
        'koin',
        'lembing',
        'kesunyian',
        'merona',
        'downfall',
        'climb',
        ]

    def get_kata():
        word = random.choice(list_kata)
        return word.upper()

    def play(word):
        progres = "_" * len(word)
        ditebak = False
        huruf_ditebak = []
        kata_ditebak = []
        percobaan = 6
        print("Game Hangman!")
        print(display_hangman(percobaan))
        print(progres)
        print("\n")
        while not ditebak and percobaan > 0:
            tebak = input("Silahkan ketik tebakan kata atau huruf: ").upper()
            if len(tebak) == 1 and tebak.isalpha():
                if tebak in huruf_ditebak:
                    print("Anda sudah menebak huruf ini", tebak)
                elif tebak not in word:
                    print(tebak, "tidak ada dalam kata.")
                    percobaan -= 1
                    huruf_ditebak.append(tebak)
                else:
                    print("Good job,", tebak, "ada di dalam kata!")
                    huruf_ditebak.append(tebak)
                    word_as_list = list(progres)
                    indeks = [i for i, letter in enumerate(word) if letter == tebak]
                    for index in indeks:
                        word_as_list[index] = tebak
                    progres = "".join(word_as_list)
                    if "_" not in progres:
                        ditebak = True
            elif len(tebak) == len(word) and tebak.isalpha():
                if tebak in kata_ditebak:
                    print("Kamu sudah menebak kata ini!", tebak)
                elif tebak != word:
                    print(tebak, "bukan kata yang benar!.")
                    percobaan -= 1
                    kata_ditebak.append(tebak)
                else:
                    ditebak = True
                    progres = word
            else:
                print("tebakan anda tidak valid.")
            print(display_hangman(percobaan))
            print(progres)
            print("\n")
        if ditebak:
            print("Selamat, kamu berhasil menebak katanya! kamu menang!")
            plusScore()
        else:
            print("Maaf, percobaan telah habis. Kata yang benar adalah " + word + ". Maybe next time!")

    def display_hangman(tries):
        stages = [  # final state: head, torso, both arms, and both legs
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / \\
               -
            """,
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / 
               -
            """,
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |      
               -
            """,
            """
               --------
               |      |
               |      O
               |     \\|
               |      |
               |     
               -
            """,
            """
               --------
               |      |
               |      O
               |      |
               |      |
               |     
               -
            """,
            """
               --------
               |      |
               |      O
               |    
               |      
               |     
               -
            """,
            """
               --------
               |      |
               |      
               |    
               |      
               |     
               -
            """
        ]
        return stages[tries]

    def main():
        word = get_kata()
        play(word)
        while input("Play Again? (Y/N) ").upper() == "Y":
            word = get_kata()
            play(word)

    if __name__ == "__main__":
        main()


def scores():
    ranks = list(sorted(users.items(), key = lambda x: getitem(x[1], 'point'), reverse=True))

    print(f'{"="*7}PAPAN SKOR{"="*7}')
    for i in range(len(ranks)):
        print(f'{i+1}. {str(ranks[i][1]["username"])}        {str(ranks[i][1]["point"])}' )


def login():
    print(f'\n{"="*7}Selamat Datang di Game Hagi{"="*7}')
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
        print("3. Hangman")
        print("4. Users Scores")
        print("5. Logout")
        print("6. Keluar")
        
        inputs = input("Pilih: ")
        if inputs == '1':
            quiz()
        elif inputs == '2':
            suit()
        elif inputs == '3':
            hangman()
        elif inputs == '4':
            scores()
        elif inputs == '5':
            login()
        elif inputs == '6':
            print("Terimakasih Telah Bermain!")
            exit()
        else:
            print("Input Salah!")


login()
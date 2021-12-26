from collections import OrderedDict
from operator import getitem

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
    print("Ini fungsi suit")

def scores():
    # ranks = sorted(users.items(), key=lambda x: x[1], reverse=True)
    # ranks = sorted(users.items(), lambda x: x[0], key=lambda x: x[1])
    #
    # for i in range(len(ranks)):
    #     print(ranks["Point"][i])

    # ranks = sorted(users, key = lambda i: i['point'])

    # ranks = sorted(users, key = lambda x: x[2]['point'])
    ranks = list(sorted(users.items(), key = lambda x: getitem(x[1], 'point'), reverse=True))
    # users[sortir]["username"]
    # ranks = sorted(users, lambda  x: x[1]['point'] == 0)
    # for i in range(len(users)):



    # for i in range(len(users)):
    #     i += 1
    #     if ranks.values() == '':
    #         ranks.update(users[i])
    #     elif i == len(users):
    #         break
    #     elif users[i+1]["point"] > users[i]["point"]:
    #         ranks.update(users[i])

    # print(str(ranks[0][1]['point']))
    # print(str(ranks[1][1]['point']))
    # print(str(ranks[2][1]['point']))
    print(f'{"="*7}PAPAN SKOR{"="*7}')
    for i in range(len(ranks)):
        print(f'{i+1}. {str(ranks[i][1]["username"])}        {str(ranks[i][1]["point"])}' )




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
        print("3. Users Scores")
        print("4. Logout")
        inputs = input("Pilih: ")
        if inputs == '1':
            quiz()
        elif inputs == '2':
            suit()
        elif inputs == '3':
            scores()
        elif inputs == '4':
            login()


login()
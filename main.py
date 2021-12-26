
def quiz():
    print("Ini fungsi kuis")

def suit():
    print("Ini fungsi suit")

def dashboard():
    while True:
        print(f'{"="*7}Selamat Datang Di Hagi!{"="*7}')
        print("1. Kuis Pengetahuan Umum")
        print("2. Batu, Gunting, Kertas")
        print("3. Keluar")
        inputs = input("Pilih: ")
        if inputs == '1':
            quiz()
        elif inputs == '2':
            suit()
        elif inputs == '3':
            print("Terimakasih Telah Bermain!")
            exit(0)

dashboard()
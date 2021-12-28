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

def decorator_with_arguments(function):
    def wrapper_accepting_arguments(arg1):
        print(f'{arg1} Mengerjakan!, Semoga Beruntung :)')
        function(arg1)
    return wrapper_accepting_arguments

@decorator_with_arguments
def welcome(hi):
    print(f'{hi} Datang di Permainan Hagi Quis!')

def quiz():
    welcome("Selamat")
    score = 0
    for question, choices, correct_choice, answer in zip(questions, answer_choices, correct_choices, answers):
        print(question)
        user_answer = input(choices).lower()
        if user_answer in correct_choice:
            print("Jawaban Benar!")
            score += 1
        else:
            print("Jawaban Salah!,", answer)
    print(score, "out of", len(questions), "that is", float(score / len(questions)) * 100, "%")

quiz()
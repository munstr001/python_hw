import random


def draw_hangman(errors):
    head = "O" if errors >= 1 else " "
    body = "|" if errors >= 2 else " "
    left_arm = "/" if errors >= 3 else " "
    right_arm = "\\" if errors >= 4 else " "
    left_leg = "/" if errors >= 5 else " "
    right_leg = "\\" if errors >= 6 else " "
    print(" +---+")
    print(" |   |")
    print(f" {head}   |")
    print(f"{left_arm}{body}{right_arm}  |")
    print(f"{left_leg} {right_leg}  |")
    print("    ===")


def play():
    words = ["питон", "компьютер", "студент", "книга", "программа", "клавиатура", "яблоко"]
    word = random.choice(words)
    letters = []
    errors = 0
    print("=== Виселица ===")
    print("Угадайте слово по буквам. Можно ошибиться 6 раз.")

    while errors < 6:
        draw_hangman(errors)
        hidden = ""
        for letter in word:
            hidden += letter if letter in letters else "_"
        print("Слово:", " ".join(hidden))
        if hidden == word:
            print("Вы победили!")
            return

        print("Названные буквы:", " ".join(letters))
        letter = input("Введите букву: ").strip().lower()
        if len(letter) != 1 or letter not in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя":
            print("Введите одну русскую букву")
            continue
        if letter in letters:
            print("Эта буква уже была")
            continue

        letters.append(letter)
        if letter not in word:
            errors += 1
            print("Такой буквы нет. Осталось попыток:", 6 - errors)

    draw_hangman(errors)
    print("Вы проиграли. Загаданное слово:", word)


if __name__ == "__main__":
    play()

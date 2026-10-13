def caesar(text, shift):
    russian = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    english = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    for char in text:
        if char.lower() in russian:
            alphabet = russian
        elif char.lower() in english:
            alphabet = english
        else:
            result += char
            continue

        if char.isupper():
            alphabet = alphabet.upper()
        index = (alphabet.index(char) + shift) % len(alphabet)
        result += alphabet[index]

    return result


if __name__ == "__main__":
    print("1 - Зашифровать\n2 - Расшифровать")
    mode = input("Выберите действие: ")
    if mode in ("1", "2"):
        text = input("Введите текст: ")
        shift = int(input("Введите сдвиг: "))
        if mode == "2":
            shift = -shift
        print("Результат:", caesar(text, shift))
    else:
        print("Такого действия нет")

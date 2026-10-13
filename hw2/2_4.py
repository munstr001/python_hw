import secrets
import string
import random


def generate_password(length, groups):
    password = []
    for group in groups:
        password.append(secrets.choice(group))

    symbols = "".join(groups)
    for i in range(length - len(password)):
        password.append(secrets.choice(symbols))

    random.SystemRandom().shuffle(password)
    return "".join(password)


if __name__ == "__main__":
    print("=== Генератор паролей ===")
    print("Ответьте да или нет на вопросы ниже\n")
    groups = []
    settings = [
        ("Добавить маленькие буквы? ", string.ascii_lowercase),
        ("Добавить большие буквы? ", string.ascii_uppercase),
        ("Добавить спецсимволы? ", "!@#$%^&*()-_+=?"),
        ("Добавить цифры? ", string.digits)
    ]

    for question, symbols in settings:
        answer = input(question).strip().lower()
        while answer not in ("да", "д", "нет", "н"):
            answer = input("Введите да или нет: ").strip().lower()
        if answer in ("да", "д"):
            groups.append(symbols)

    if not groups:
        print("Нужно выбрать хотя бы один тип символов")
    else:
        length = input("Длина пароля: ").strip()
        while not length.isdecimal() or int(length) < len(groups):
            length = input(f"Введите целое число не меньше {len(groups)}: ").strip()
        print("\nВаш пароль:", generate_password(int(length), groups))

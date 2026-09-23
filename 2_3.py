def print_pack_report(number):
    for i in range(number, 0, -1):
        if i % 3 == 0 and i % 5 == 0:
            print(i, "- расфасуем по 3 или по 5")
        elif i % 5 == 0:
            print(i, "- расфасуем по 5")
        elif i % 3 == 0:
            print(i, "- расфасуем по 3")
        else:
            print(i, "- не заказываем!")


if __name__ == "__main__":
    number = int(input("Введите количество пирожных (больше 1): "))
    if number > 1:
        print_pack_report(number)
    else:
        print("Нужно число больше 1")

def to_roman(number):
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    result = ""
    for value, symbol in zip(values, symbols):
        while number >= value:
            result += symbol
            number -= value
    return result


def from_roman(text):
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    for i in range(len(text)):
        if text[i] not in values:
            return None
    for i in range(len(text)):
        if i + 1 < len(text) and values[text[i]] < values[text[i + 1]]:
            result -= values[text[i]]
        else:
            result += values[text[i]]
    if 1 <= result <= 3999 and to_roman(result) == text:
        return result
    return None


if __name__ == "__main__":
    print("=== Римский конвертер ===")
    text = input("Введите число от 1 до 3999 или римское число: ").strip().upper()
    if text.isdecimal():
        number = int(text)
        if 1 <= number <= 3999:
            print(to_roman(number))
        else:
            print("Нужно число от 1 до 3999")
    else:
        number = from_roman(text)
        if number is None:
            print("Неверная запись римского числа")
        else:
            print(number)

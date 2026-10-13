string = input("Введите строку: ")
dictionary = {}
for char in string:
    if char in dictionary:
        dictionary[char] += 1
    else:
        dictionary[char] = 1

for i in (sorted(dictionary.items(), key=lambda item: item[1], reverse=True)[:3]):
    print(f"{i[0]} - {i[1]}")
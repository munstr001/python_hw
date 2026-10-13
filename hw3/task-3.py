from datetime import date


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        return f'{self.title}, {self.author}, {self.year} г.'

    def __str__(self):
        return self.info()

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return (self.title, self.author, self.year) == (other.title, other.author, other.year)

    @property
    def age(self):
        return date.today().year - self.year

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError('Возраст должен быть целым неотрицательным числом')
        self.year = date.today().year - value

    @classmethod
    def from_string(cls, text):
        title, author, year = text.split(';')
        return cls(title.strip(), author.strip(), int(year))


if __name__ == '__main__':
    book = Book('Дубровский', 'Александр Пушкин', 1841)
    other = Book.from_string('Дубровский; Александр Пушкин; 1841')
    print(book)
    print('Одинаковые книги:', book == other)
    print('Возраст:', book.age)
    other.age = 10
    print('Год после изменения возраста:', other.year)

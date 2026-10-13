from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def print_info(self):
        pass


class Book(Printable):
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        return f'{self.title}, {self.author}, {self.year} г.'

    def print_info(self):
        print(self.info())


if __name__ == '__main__':
    book = Book('Герой нашего времени', 'Михаил Лермонтов', 1840)
    book.print_info()

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        return f'{self.title}, {self.author}, {self.year} г.'


class Ebook(Book):
    def __init__(self, title, author, year, format):
        super().__init__(title, author, year)
        self.format = format

    def info(self):
        return f'{super().info()}, формат: {self.format}'


if __name__ == '__main__':
    book = Ebook('Капитанская дочка', 'Александр Пушкин', 1836, 'epub')
    print(book.info())

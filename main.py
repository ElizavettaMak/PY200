class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.__name = name
        self.__author = author

    def __str__(self):
        return f"Книга {self.__name}. Автор {self.__author}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.__validate_pages(pages)
        self.__pages = pages

    @staticmethod
    def __validate_pages(pages):
        if not isinstance(pages, int):
            raise TypeError()
        if pages <= 0:
            raise ValueError()

    @property
    def pages(self):
        return self.__pages

    def __str__(self):
        return Book.__str__(self) + f" Количество страниц {self.pages}."

    def __repr__(self):
        return Book.__repr__(self) + f" pages={self.__pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.__validate_duration(duration)
        self.__duration = duration

    @staticmethod
    def __validate_duration(duration):
        if not isinstance(duration, int):
            raise TypeError()
        if duration <= 0:
            raise ValueError()

    @property
    def duration(self):
        return self.__duration

    def __str__(self):
        return Book.__str__(self) + f" Продолжительность {self.duration}."

    def __repr__(self):
        return Book.__repr__(self) + f" duration={self.duration!r})"

if __name__ == "__main__":
    book1 = Book(name='Имя 1', author='Автор 1')
    book2 = Book(name='Имя 2', author='Автор 2')
    #book3 = PaperBook(name='Имя 3', author='Автор 3', pages='Кол-во стр 3')
    book4 = PaperBook(name='Имя 4', author='Автор 4', pages=100)
    #book5 = AudioBook(name='Имя 5', author='Автор 5', duration='Продилжительность 5')
    book6 = AudioBook(name='Имя 6', author='Автор 6', duration=120)
    print(book1.__str__())
    print(book1.__repr__())
    print(book4.__str__())
    print(book4.__repr__())
    print(book6.__str__())
    print(book6.__repr__())
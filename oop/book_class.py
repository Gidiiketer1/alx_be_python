class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"


class EBook(Book):
    def __init__(self, title, author, publication_year, file_size):
        super().__init__(title, author, publication_year)
        self.file_size = file_size  # in MB

    def __str__(self):
        return f"EBook: {super().__str__()} [{self.file_size}MB]"


class PrintBook(Book):
    def __init__(self, title, author, publication_year, weight):
        super().__init__(title, author, publication_year)
        self.weight = weight  # in grams

    def __str__(self):
        return f"PrintBook: {super().__str__()} [{self.weight}g]"

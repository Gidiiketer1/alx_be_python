from book_class import Book, EBook, PrintBook

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        if not self.books:
            print("Library is empty.")
        else:
            for book in self.books:
                print(book)

    def __str__(self):
        return f"Library has {len(self.books)} book(s)."

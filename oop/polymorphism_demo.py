from book_class import EBook, PrintBook

def show_book_info(book):
    print(book)

if __name__ == "__main__":
    ebook = EBook("Python Mastery", "Gideon Kipngetich", 2023, 5)
    printbook = PrintBook("Clean Code", "Robert C. Martin", 2008, 300)

    show_book_info(ebook)
    show_book_info(printbook)

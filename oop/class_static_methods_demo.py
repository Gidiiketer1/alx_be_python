class BookUtils:
    total_books_created = 0

    def __init__(self, title):
        self.title = title
        BookUtils.total_books_created += 1

    @classmethod
    def get_total_books(cls):
        return cls.total_books_created

    @staticmethod
    def is_valid_title(title):
        return isinstance(title, str) and len(title) > 0


if __name__ == "__main__":
    print("Creating books...")
    b1 = BookUtils("OOP in Python")
    b2 = BookUtils("Design Patterns")

    print(f"Total books created: {BookUtils.get_total_books()}")
    print(f"Is 'Python' a valid title? {BookUtils.is_valid_title('Python')}")

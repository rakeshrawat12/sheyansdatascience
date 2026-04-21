class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def show_books(self):
        print("Books:", self.books)

lib = Library()
lib.add_book("Python")
lib.add_book("DSA")
lib.show_books()
lib.remove_book("Python")
lib.show_books()
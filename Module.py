class Book:
    def __init__(self, name, id, author):
        self.name = name
        self.id = id
        self.author = author

class Library:
    def __init__(self):
        self.Books = {}
        self.initializeBooks()

    def initializeBooks(self):
        book0 = Book("To all the boys i loved Before", "000", "Jenny Han")
        book1 = Book("Me before You", "001", "Jojo Moyes")
        book2 = Book("Ugly Love", "002", "Collen Hoover")
        book3 = Book("From Lukov, with Love", "003", "Mariana Zapata")
        book4 = Book("The summer i turned Pretty", "004", "Jenny Han")
        book5 = Book("Pride and Prejudice", "005", "Jane Austen")
        book6 = Book("The notebook", "006", "Nicholas Sparks")
        book7 = Book("It Ends with Us", "007", "Collen Hoover")
        book8 = Book("The Love Hypothesis", "008", "Ali Hazelwood")

        self.add_book(book0)
        self.add_book(book1)
        self.add_book(book2)
        self.add_book(book3)
        self.add_book(book4)
        self.add_book(book5)
        self.add_book(book6)
        self.add_book(book7)
        self.add_book(book8)

    def add_book(self, book):
        self.Books[book.id] = book

    def order_book(self, book_id):
        if book_id in self.Books:
            book = self.Books[book_id]
            if book.available:
                book.available = False
                print(f"Book '{book.name}' ordered successfully.")
            else:
                print(f"Book '{book.name}' is not available for order.")
        else:
            print(f"Book with ID {book_id} not found in the library.")

    def find_book_by_name(self, book_name):
        for book in self.Books.values():
            if book.name.lower() == book_name.lower():
                return book
        return None

library = Library()


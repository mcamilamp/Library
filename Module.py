class Book:
    def __init__(self, name, id, author, genre):
        self.name = name
        self.id = id
        self.author = author
        self.genre = genre
        self.available = True


class Library:
    def __init__(self):
        self.Books = {}
        self.initializeBooks()


    def initializeBooks(self):
        book0 = Book("To all the boys i loved Before", "000", "Jenny Han", "Romantic")
        book1 = Book("Me before You", "001", "Jojo Moyes", "Romantic")
        book2 = Book("The Selection", "002", "Kiera Cass", "Romantic")
        book3 = Book("Little House on the Prairie ", "003", "Laura Ingalls Wilder", "Autobiography")
        book4 = Book("Ugly Love", "004", "Collen Hoover", "Romantic")
        book5 = Book("From Lukov, with Love", "005", "Mariana Zapata", "Romantic")
        book6 = Book("The summer i turned Pretty", "006", "Jenny Han", "Romantic")
        book7 = Book("Pride and Prejudice", "007", "Jane Austen", "Romantic")
        book8 = Book("The notebook", "008", "Nicholas Sparks", "Romantic")
        book9 = Book("It Ends with Us", "009", "Collen Hoover", "Romantic")
        book10 = Book("The Love Hypothesis", "010", "Ali Hazelwood", "Romantic")
        book11 = Book("The Diary of a Young Girl", "011", "Anne", "Autobiography")
        book12 = Book("Love on the Brain", "012", "Ali Hazelwood", "Romantic")
        book13 = Book("The One", "013", "Kiera Cass", "Romantic")
        book14 = Book("Obsidian ", "014", "Jennifer L. Armentrout", "Fiction")
        book15 = Book("Onyx", "015", "Jennifer L. Armentrout", "Fiction")
        book16 = Book("Macondo", "016", "Gabriel Garcia Marquez", "Magical realism")
        book17 = Book("Dracula", "017", "Bram Stoker", "terror")
        book18 = Book("Frankenstein", "018", "Mary Shelley", "terror")
        book19 = Book("A walk to remember", "019", "Nicholas Sparks", "Romantic")


        self.add_book(book0)
        self.add_book(book1)
        self.add_book(book2)
        self.add_book(book3)
        self.add_book(book4)
        self.add_book(book5)
        self.add_book(book6)
        self.add_book(book7)
        self.add_book(book8)
        self.add_book(book9)
        self.add_book(book10)
        self.add_book(book11)
        self.add_book(book12)
        self.add_book(book13)
        self.add_book(book14)
        self.add_book(book15)
        self.add_book(book16)
        self.add_book(book17)
        self.add_book(book18)
        self.add_book(book19)


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
    

class Filter:
    def filter(self, books: list[Book]) -> list[Book]:
        return books
    

class GenreFilter(Filter):
    genre = str
    def __init__(self, genre) -> None:
        self.genre = genre 

    def filter(self, books: dict[str, Book])-> list[Book]:
        res = []
        for book in books:
            if books[book].genre.lower()==self.genre.lower():
                res.append(books[book])

        return res 
    
            
class AuthorFilter(Filter):
    author = str
    def __init__(self, author) -> None:
        self.author = author
    
    def filter(self, books: dict[str, Book])-> list[Book]:
        res = []
        for book in books:
             if books[book].author.lower()==self.author.lower():
                res.append(books[book])

        return res 


library = Library()



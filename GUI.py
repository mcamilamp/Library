from tkinter import *
from tkinter import messagebox
from Module import Library, Book, Filter, AuthorFilter, GenreFilter 

library = Library()

def order_book():
    selected_book = entry.get().strip()
    if selected_book:
        book = library.find_book_by_name(selected_book)
        if book:
            library.order_book(book.id)
            messagebox.showinfo("Order", f"Yes, the book: '{book.name}' is available \n\nBook Information:\n\nAuthor: '{book.author}' \nID: '{book.id}' \nGenre: '{book.genre}' ")
            entry.delete(0, END)
        else:
            messagebox.showinfo("Information", f"The book '{selected_book}' is not available")
            
def filter_by_genre():
    selected_genre = Genre_entry.get().strip()
    if selected_genre:
        filter = GenreFilter(selected_genre)
        books: list[Book] = filter.filter(library.Books)
        if len(books)== 0:
            messagebox.showinfo("Info", f"There no book with genre: '{selected_genre}'")
        else:
            message = f"Book of genre '{selected_genre}': \n\n"
            for book in books:
                message += f"-{book.name} - {book.author}\n"
            messagebox.showinfo("Info", message)

def filter_by_author():
    selected_author = Author_entry.get().strip()
    if selected_author:
        filter = AuthorFilter(selected_author)
        books: list[Book] = filter.filter(library.Books)
        if len(books)==0:
            messagebox.showinfo("Info", f"There no book with Author: '{selected_author}'")
        else:
            message = f"Book of Author '{selected_author}': \n\n"
            for book in books:
                message += f"-{book.name} - {book.author}\n"
            messagebox.showinfo("Info", message)

window = Tk()
window.title("Library: Under the Tree")
window.geometry("560x600")
window.configure(background="#cdd9ff")
iconimage = PhotoImage(file="tree_489969.png")
window.iconphoto(False, iconimage)

title = Label(window, text="Under the Tree", font=('bold', 20))
title.place(x=180, y=10)

img = PhotoImage(file="tree.png")
img = img.subsample(2)

image_label = Label(window, image=img)
image_label.place(x=150, y=60)

# ///////////////////////////////////////////////////////////

entry_label = Label(window, text="Enter the name of the book:")
entry_label.place(x=110, y=340)

entry = Entry(window)
entry.place(x=110, y=370)

show_books_btn = Button(window, text="Verify existence", command=order_book)
show_books_btn.place(x=110, y=400)

# //////////////////////////////////////////////////////////

entry_label2 = Label(window, text="Show books by genre:")
entry_label2.place(x=110, y=450)

Genre_entry = Entry(window)
Genre_entry.place(x=110, y=480)

show_author_btn = Button(window, text="Show Books", command=filter_by_genre)
show_author_btn.place(x=110, y=508)

# //////////////////////////////////////////////////////////

entry_label3 = Label(window, text="Show books by Author:")
entry_label3.place(x=310, y=450)

Author_entry = Entry(window)
Author_entry.place(x=310, y=480)

show_genre_btn = Button(window, text="Show Books", command=filter_by_genre)
show_genre_btn.place(x=310, y=508)
window.mainloop()
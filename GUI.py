from tkinter import *
from tkinter import messagebox
from Module import Library 

library = Library()

def order_book():
    selected_book = entry.get().strip()
    if selected_book:
        book = library.find_book_by_name(selected_book)
        if book:
            library.order_book(book.id)
            messagebox.showinfo("Order", f"You ordered the book: {book.name}")
            entry.delete(0, END)
        else:
            messagebox.showinfo("Information", f"The book '{selected_book}' is not available")

window = Tk()
window.title("Library: Under the Tree")
window.geometry("500x500")
window.configure(background="#cdd9ff")

title = Label(window, text="Under the Tree", font=('bold', 20))
title.place(x=154, y=10)

img = PhotoImage(file="tree.png")
img = img.subsample(2)

image_label = Label(window, image=img)
image_label.place(x=125, y=60)

entry_label = Label(window, text="Enter the name of the book you want to borrow:")
entry_label.place(x=110, y=340)

entry = Entry(window)
entry.place(x=110, y=370)

button1 = Button(window, text="Order a book", command=order_book)
button1.place(x=200, y=410)

window.mainloop()
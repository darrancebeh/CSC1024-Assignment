from aux1_get_books import get_books
from input_to_isbn import input_to_isbn
from F1_display_books import display_books
from isbn_to_details import isbn_to_details


def delete_book_interface():

    book_list = get_books()

    display_books()

    delete_book(isbn_to_details(input_to_isbn()))


def delete_book(isbn):

    book_list = get_books()

    for book in book_list:
        book = book.split("|")
        if isbn in book[0]:
            book_list.remove("|".join(book))
            break

    with open("books_23094907.txt", "w") as f:
        for book in book_list:
            f.write(book)
            f.write("\n")

    print("Book Deleted Successfully!")


delete_book_interface()

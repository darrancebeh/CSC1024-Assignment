from get_books import get_books
from input_to_isbn import input_to_isbn


def delete_book_interface():

    book_list = get_books()

    for book in book_list:
        print(book)

    user_input_id = input_to_isbn()

    if (user_input_id == 1):
        delete_book_interface()
    elif (user_input_id == 0):
        print("Main Menu Function haha")
        exit()

    delete_book(user_input_id)


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

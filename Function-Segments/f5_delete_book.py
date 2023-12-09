from aux1_get_books import get_books
from aux4_input_to_isbn import input_to_isbn
from f1_display_books import display_books

import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def delete_book_interface():
    clear()

    print(r'''
          
██████╗░███████╗██╗░░░░░███████╗████████╗███████╗  ██████╗░░█████╗░░█████╗░██╗░░██╗
██╔══██╗██╔════╝██║░░░░░██╔════╝╚══██╔══╝██╔════╝  ██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
██║░░██║█████╗░░██║░░░░░█████╗░░░░░██║░░░█████╗░░  ██████╦╝██║░░██║██║░░██║█████═╝░
██║░░██║██╔══╝░░██║░░░░░██╔══╝░░░░░██║░░░██╔══╝░░  ██╔══██╗██║░░██║██║░░██║██╔═██╗░
██████╔╝███████╗███████╗███████╗░░░██║░░░███████╗  ██████╦╝╚█████╔╝╚█████╔╝██║░╚██╗
╚═════╝░╚══════╝╚══════╝╚══════╝░░░╚═╝░░░╚══════╝  ╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝

██╗███╗░░██╗████████╗███████╗██████╗░███████╗░█████╗░░█████╗░███████╗
██║████╗░██║╚══██╔══╝██╔════╝██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝
██║██╔██╗██║░░░██║░░░█████╗░░██████╔╝█████╗░░███████║██║░░╚═╝█████╗░░
██║██║╚████║░░░██║░░░██╔══╝░░██╔══██╗██╔══╝░░██╔══██║██║░░██╗██╔══╝░░
██║██║░╚███║░░░██║░░░███████╗██║░░██║██║░░░░░██║░░██║╚█████╔╝███████╗
╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚══════╝''')

    print("\n______________________________________________________________________________\n")

    display_books()

    user_input = input_to_isbn()

    if (user_input == 1):
        delete_book_interface()
    elif (user_input == 0):
        return
    else:
        delete_book(user_input)


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

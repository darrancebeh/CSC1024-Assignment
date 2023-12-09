from aux1_get_books import get_books
from aux4_input_to_isbn import input_to_isbn
from f1_display_books import display_books
from aux5_isbn_to_details import isbn_to_details

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
        book_details = isbn_to_details(user_input)

        # display targeted book details
        print("\n______________________________________________________________________________\n")
        print("Book Details:")
        print("ISBN: " + book_details[0])
        print("Author: " + book_details[1])
        print("Title: " + book_details[2])
        print("Publisher: " + book_details[3])
        print("Genre: " + book_details[4])
        print("Year Published: " + book_details[5])
        print("Date Purchased: " + book_details[6])
        print("Status: " + book_details[7])
        print("\n______________________________________________________________________________\n")

        '''
        Double confirms with user to confirm whether they want to delete the selected book.
        '''
        user_option = input(
            "Are you sure you want to delete this book?\n[1] - Yes\n[2] - No\n")

        # error handling
        if (user_option not in ['1', '2']):
            print("Invalid Input!")
            user_option = input(
                "Are you sure you want to delete this book?\n[1] - Yes\n[2] - No\n")

        # deletes book if user confirms, otherwise returns to main menu
        if (user_option == "Y" or user_option == "1"):
            delete_book(user_input)
        elif (user_option == "N" or user_option == "2"):
            print("Okay. The Book will not be Deleted.")
            input("Press Any Key to Return to Main Menu.")
            return 0


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

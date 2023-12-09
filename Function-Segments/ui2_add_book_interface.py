'''
- The os module is imported to provide a way of using operating system-dependent functionality.
- Other modules are imported for additional resources.
'''
import os
from f3_add_book import add_book_information
from f3_add_book import add_book
from f1_display_books import display_books

'''
- Clears the screen for better visibility.
'''


def clear():
    os.system("cls" if os.name == "nt" else "clear")


'''
- Calls the clear function to clear the screen for better visibility. 
- Displays header for the function (adding books).
'''


def add_book_interface():
    clear()
    print(
        r"""
██████╗░░█████╗░░█████╗░██╗░░██╗  ░█████╗░██████╗░██████╗░██╗████████╗██╗░█████╗░███╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝  ██╔══██╗██╔══██╗██╔══██╗██║╚══██╔══╝██║██╔══██╗████╗░██║
██████╦╝██║░░██║██║░░██║█████═╝░  ███████║██║░░██║██║░░██║██║░░░██║░░░██║██║░░██║██╔██╗██║
██╔══██╗██║░░██║██║░░██║██╔═██╗░  ██╔══██║██║░░██║██║░░██║██║░░░██║░░░██║██║░░██║██║╚████║
██████╦╝╚█████╔╝╚█████╔╝██║░╚██╗  ██║░░██║██████╔╝██████╔╝██║░░░██║░░░██║╚█████╔╝██║░╚███║
╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝  ╚═╝░░╚═╝╚═════╝░╚═════╝░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝

██╗███╗░░██╗████████╗███████╗██████╗░███████╗░█████╗░░█████╗░███████╗
██║████╗░██║╚══██╔══╝██╔════╝██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝
██║██╔██╗██║░░░██║░░░█████╗░░██████╔╝█████╗░░███████║██║░░╚═╝█████╗░░
██║██║╚████║░░░██║░░░██╔══╝░░██╔══██╗██╔══╝░░██╔══██║██║░░██╗██╔══╝░░
██║██║░╚███║░░░██║░░░███████╗██║░░██║██║░░░░░██║░░██║╚█████╔╝███████╗
╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚══════╝
"""
    )

    print("\nWelcome to the Book Addition Interface!\n")

    '''
    - Display all books using display_books().
    - Prompts the user to input details for a new book by calling the add_book_information() function.
    - Attempts to add the new book to the collection using the add_book() function. If an error occurs during this process, it prints an error message and returns.
    - If the book is added successfully, it prints a success message and the details of the new book.
    - Ask the user if they want to add another book. If they do, it calls itself recursively to repeat the process. If not, it returns 0 to end the function.
    '''

    display_books()

    print("_____________________________________")
    print(f"\nAll books have been displayed.\n")
    print("To add a book, please input the book's details.\n")

    try:
        book = add_book_information()
        isbn, author, title, publisher, genre, yop, dop, status = book
        add_book(book)
    except Exception as e:
        print(f"An error occurred while adding the book: {str(e)}")

    print(
        "\nCongratulations! Your Input is Valid and A Book Has Been Added!\n"
    )

    print(f"\nBook Added: {title} by {author}")
    print("\nBook Details:\n")
    print(f"ISBN: {isbn}")
    print(f"Author: {author}")
    print(f"Title: {title}")
    print(f"Publisher: {publisher}")
    print(f"Genre: {genre}")
    print(f"Year of Publication: {yop}")
    print(f"Date of Purchase: {dop}")
    print(f"Status: {status}")

    print("\nWould You Like to Add Another Book?\n")
    user_input_option = input("[1] - Yes\n[2] - No\n\n")

    while user_input_option not in ["1", "2"]:
        print("\nWould You Like to Add Another Book?\n")
        user_input_option = input(
            "[1] - Yes, Retry the Function\n[2] - No, Return to Main Menu.\n\n"
        )

    if user_input_option == "1":
        add_book_interface()

    '''
    - Calls the add_book_interface() function to start the process.
    '''


add_book_interface()

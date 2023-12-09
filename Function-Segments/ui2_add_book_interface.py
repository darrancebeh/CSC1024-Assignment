'''
- The os module is imported to provide a way of using operating system-dependent functionality.
- The statement `from datetime import datetime` is used to directly import the `datetime` class from the `datetime` module. It is commonly used for handling dates and times.
'''


import os
from f3_add_book import add_book
from f1_display_books import display_books
from f3_add_book import check_isbn_duplicate

from datetime import datetime

'''
- Clears the screen for better visibility.
'''


def clear():
    os.system("cls" if os.name == "nt" else "clear")


'''
- Calls the clear function to clear the screen for better visibility. 
- Displays header for the function (adding books).
'''

'''
- The 'add_book_information()' function collects and validates information about a book from the user.
- It prompts the user to enter the ISBN, author's name, book's title, publisher's name, genre, publishing year, purchase date, and book status.
- The naming convention is taken into consideration as people from different cultures have different naming conventions, such as umlauts and ligatures.
- Also performs validation checks for the ISBN to detect existing matching books.
'''


def add_book_information():
    print("Please enter the following information:")
    while True:
        isbn = input("ISBN number: ")
        if len(isbn) == 13 and isbn.isdigit():
            if check_isbn_duplicate(isbn):
                print("Error. A book with this ISBN already exists.")
                continue
            else:
                break
        else:
            print(
                "Error. ISBN must be 13 digits long and contain only digits. Please try again.")
    while True:
        author = input("Author's name: ")
        if all(word.isalpha() for word in author.split()):
            break
        else:
            print(
                "Error. The author's name must only contain alphabetical characters. Please try again.")
    title = input("Book's title: ")
    publisher = input("Publisher's name: ")
    while True:
        genre = input("Genre of the book: ")
        if all(word.isalpha() for word in genre.split()):
            break
        else:
            print(
                "Error. The genre must only contain alphabetical characters. Please try again.")
    while True:
        published_year = input("Publishing year: ")
        if len(published_year) == 4 and published_year.isdigit() and int(published_year) > 0 and int(published_year) <= datetime.now().year:
            published_date = datetime(int(published_year), 1, 1)
            break
        else:
            print("Error. Publishing year must be a 4-digit positive integer and not in the future. Please try again.")
    while True:
        date_purchased_str = input("Date purchased in the format DD/MM/YYYY: ")
        if len(date_purchased_str) != 10:
            print(
                "Error. The date must be exactly 10 characters long in the format DD/MM/YYYY. Please try again.")
            continue
        try:
            date_purchased = datetime.strptime(date_purchased_str, '%d/%m/%Y')
            if date_purchased <= datetime.now() and date_purchased > published_date:
                break
            else:
                print(
                    "Error. The purchase date must be after the publishing year. Please try again.")
        except ValueError:
            print("Error. The date format is incorrect. Please try again.")
    while True:
        print("Please input the book's status:")
        print("[1] - wishlist")
        print("[2] - to-read")
        print("[3] - reading")
        print("[4] - completed")
        print()
        status_input = input("Book's status (enter a number from 1 to 4): ")
        status_options = {'1': 'wishlist', '2': 'to-read',
                          '3': 'reading', '4': 'completed'}
        if status_input in status_options:
            status = status_options[status_input]
            break
        else:
            print("Error. Invalid status. Please try again.")

    book_details = (isbn, author, title, publisher, genre,
                    published_year, date_purchased_str, status)
    return book_details


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
    except Exception as e:
        print(f"An error occurred while adding the book: {str(e)}")

    '''
    Prints details of the book to add and double confirms with user whether they want to add the book.
    '''

    print("\n_____________________________________")
    print("\nPlease confirm the following details:\n")
    print(f"ISBN: {isbn}")
    print(f"Author: {author}")
    print(f"Title: {title}")
    print(f"Publisher: {publisher}")
    print(f"Genre: {genre}")
    print(f"Year of Publication: {yop}")
    print(f"Date of Purchase: {dop}")
    print(f"Status: {status}")

    print("\n_____________________________________")

    user_input_confirm = input(
        "\nAre you sure you want to add this book with the following details?\n[1] - Yes\n[2] - No\n\n")

    while user_input_confirm not in ["1", "2"]:
        print("\nAre you sure you want to add this book with the following details?\n")
        user_input_confirm = input(
            "\nAre you sure you want to add this book with the following details?\n[1] - Yes\n[2] - No\n\n")

    if (user_input_confirm == "1"):
        add_book(book)
    else:
        print("Okay. The Book will not be Added.")
        input("Press Any Key to Return to Main Menu.")
        return 0

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

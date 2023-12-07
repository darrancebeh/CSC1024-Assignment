import os

from get_books import get_books
from user_error_option import user_error_redirect
from update_book import update_book
from check_author_multiple_book import check_author_multiple_book
from input_to_isbn import input_to_isbn
from display_books import display_books


def clear():
    '''
    Clears the Screen for better visibility.
    '''

    os.system('cls' if os.name == 'nt' else 'clear')


def update_book_interface():
    '''
    Calls the clear function to clear the screen for better visiblity.
    Displays header for the function. (Book Update)
    '''

    clear()
    print(r"""
██████╗░░█████╗░░█████╗░██╗░░██╗  ██╗░░░██╗██████╗░██████╗░░█████╗░████████╗███████╗
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝  ██║░░░██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
██████╦╝██║░░██║██║░░██║█████═╝░  ██║░░░██║██████╔╝██║░░██║███████║░░░██║░░░█████╗░░
██╔══██╗██║░░██║██║░░██║██╔═██╗░  ██║░░░██║██╔═══╝░██║░░██║██╔══██║░░░██║░░░██╔══╝░░
██████╦╝╚█████╔╝╚█████╔╝██║░╚██╗  ╚██████╔╝██║░░░░░██████╔╝██║░░██║░░░██║░░░███████╗
╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝  ░╚═════╝░╚═╝░░░░░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝

██╗███╗░░██╗████████╗███████╗██████╗░███████╗░█████╗░░█████╗░███████╗
██║████╗░██║╚══██╔══╝██╔════╝██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝
██║██╔██╗██║░░░██║░░░█████╗░░██████╔╝█████╗░░███████║██║░░╚═╝█████╗░░
██║██║╚████║░░░██║░░░██╔══╝░░██╔══██╗██╔══╝░░██╔══██║██║░░██╗██╔══╝░░
██║██║░╚███║░░░██║░░░███████╗██║░░██║██║░░░░░██║░░██║╚█████╔╝███████╗
╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚══════╝""")

    print("\nWelcome to the Book Updating Interface!\n")

    '''
    Displays all books in database.
    Allows user to clearly know what books are in the database and what details to update.
    '''
    display_books()

    '''
    Prompts user to input ISBN, author or title.
    '''

    print("_____________________________________")
    print(f"\nAll Books Have Been Displayed.\n")
    print("To Edit an Item, Please Input the Item's 13-digit ISBN, Author OR Book Title.\n")

    user_input_id = input_to_isbn()

    '''
    If user input is valid,
    Run through book list to find book with same ISBN, author or title.
    Displays details of books and prompts user input for what details to update.
    Also Clears screen for better visibility.
    '''

    clear()
    print(r"""       
██████╗░░█████╗░░█████╗░██╗░░██╗  ███████╗░█████╗░██╗░░░██╗███╗░░██╗██████╗░██╗
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝  ██╔════╝██╔══██╗██║░░░██║████╗░██║██╔══██╗██║
██████╦╝██║░░██║██║░░██║█████═╝░  █████╗░░██║░░██║██║░░░██║██╔██╗██║██║░░██║██║
██╔══██╗██║░░██║██║░░██║██╔═██╗░  ██╔══╝░░██║░░██║██║░░░██║██║╚████║██║░░██║╚═╝
██████╦╝╚█████╔╝╚█████╔╝██║░╚██╗  ██║░░░░░╚█████╔╝╚██████╔╝██║░╚███║██████╔╝██╗
╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝  ╚═╝░░░░░░╚════╝░░╚═════╝░╚═╝░░╚══╝╚═════╝░╚═╝
""")
    print("\nCongratulations! Your Input is Valid and A Book Has Been Found!\n")

    # gets all books in database
    book_list = get_books()

    # initialize isbn_list to check for duplicate isbn when updating isbn
    isbn_list = []

    for book in book_list:

        # temp variables assigned because we only use this for loop to search for the specific user-inputted book
        temp_isbn, temp_author, temp_title, temp_publisher, temp_genre, temp_yop, temp_dop, temp_status = book.split(
            "|")

        # adds every book's isbn into isbn_list to check for duplicate isbn when updating isbn
        isbn_list.append(temp_isbn)

        if (temp_isbn == user_input_id or temp_author == user_input_id or temp_title == user_input_id):

            # assigns temp variables to actual variables if book is found
            isbn = temp_isbn
            author = temp_author
            title = temp_title
            publisher = temp_publisher
            genre = temp_genre
            yop = temp_yop
            dop = temp_dop
            status = temp_status

            # displays book details
            print(f"\nBook Found: {title} by {author}")
            print("\nBook Details:\n")
            print(f"ISBN: {isbn}")
            print(f"Author: {author}")
            print(f"Title: {title}")
            print(f"Publisher: {publisher}")
            print(f"Genre: {genre}")
            print(f"Year of Publication: {yop}")
            print(f"Date of Purchase: {dop}")
            print(f"Status: {status}")

    print("\n\nWhat Details Would You Like to Update?\n")
    user_update_option = input(
        "[1] - ISBN\n[2] - Author\n[3] - Title\n[4] - Publisher\n[5] - Genre\n[6] - Year of Publication\n[7] - Date of Purchase\n[8] - Book Status\n\n")

    if (user_update_option not in ['1', '2', '3', '4', '5', '6', '7', '8']):
        if (user_error_redirect("\nERROR: Invalid Input Detected. Please Input an Option between [1] - [4].")):
            update_book_interface()
        else:
            return 0

    else:
        if (user_update_option == '1'):
            new_isbn = input(
                "Please Input New ISBN (13 Digits):\n")

            if (len(new_isbn) != 13):
                if (user_error_redirect(f"\nERROR: ISBN Should Contain EXACTLY 13 digits. Your Input Had {len(new_isbn)} digits.")):
                    update_book_interface()
                else:
                    return 0
            else:
                if (new_isbn in isbn_list):
                    if (user_error_redirect(f"\nERROR: ISBN {new_isbn} Already Exists in Database.")):
                        update_book_interface()
                    else:
                        return 0

                else:
                    update_book(
                        isbn, new_isbn, "isbn")

        elif (user_update_option == '2'):
            print(
                f"Current Author: {author}\n")
            new_author = input(
                "Please Input New Author:\n")
            update_book(
                author, new_author, "author")

        elif (user_update_option == '3'):
            print(
                f"Current Title: {title}\n")
            new_title = input(
                "Please Input New Title:\n")
            update_book(
                title, new_title, "title")

        elif (user_update_option == '4'):
            print(
                f"Current Publisher: {publisher}\n")
            new_publisher = input(
                "Please Input New Publisher:\n")
            update_book(
                publisher, new_publisher, "publisher")

        elif (user_update_option == '5'):
            print(
                f"Current Genre: {genre}\n")
            new_genre = input(
                "Please Input New Genre:\n")
            update_book(
                genre, new_genre, "genre")

        elif (user_update_option == '6'):
            print(
                f"Current Year of Publication: {yop}\n")
            new_yop = input(
                "Please Input New Year of Publication:\n")
            if (len(new_yop) != 4):
                if (user_error_redirect(f"\nERROR: Year of Publication Should Contain EXACTLY 4 digits. Your Input Had {len(new_yop)} digits.")):
                    update_book_interface()
                else:
                    return 0
            update_book(
                yop, new_yop, "yop")

        elif (user_update_option == '7'):
            print(
                f"Current Date of Purchase: {dop}\n")
            new_dop = input(
                "Please Input New Date of Purchase:\n")
            update_book(
                dop, new_dop, "dop")

        elif (user_update_option == '8'):
            print(
                f"Current Status: {status}\n")
            new_status = input(
                "Please Input New Status:\n[1] - Wishlist\n[2] - To-Read\n[3] - Reading\n[4] - Completed\n\n")

            if (new_status not in ["1", "2", "3", "4"]):
                if (user_error_redirect("\nERROR: Invalid Input Detected. Please Input an Option between [1] - [4].")):
                    update_book_interface()
                else:
                    return 0

            if (new_status == '1'):
                new_status = "wishlist"
            elif (new_status == '2'):
                new_status = "to-read"
            elif (new_status == '3'):
                new_status = "reading"
            else:
                new_status = "completed"

            update_book(
                status, new_status, "status")


update_book_interface()

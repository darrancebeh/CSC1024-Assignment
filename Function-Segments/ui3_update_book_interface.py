import os

from aux1_get_books import get_books
from aux3_user_error_option import user_error_redirect
from f4_update_book import update_book
from aux2_check_author_multiple_book import check_author_multiple_book
from aux4_input_to_isbn import input_to_isbn
from f1_display_books import display_books
from aux5_isbn_to_details import isbn_to_details


def clear():
    """
    Clears the Screen for better visibility.
    """

    os.system("cls" if os.name == "nt" else "clear")


def update_book_interface():
    """
    Calls the clear function to clear the screen for better visiblity.
    Displays header for the function. (Book Update)
    """

    clear()
    print(
        r"""
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
╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚══════╝"""
    )

    print("\nWelcome to the Book Updating Interface!\n")

    """
    Displays all books in database.
    Allows user to clearly know what books are in the database and what details to update.
    """
    display_books()

    """
    Prompts user to input ISBN, author or title.
    """

    print("_____________________________________")
    print(f"\nAll Books Have Been Displayed.\n")
    print(
        "To Edit an Item, Please Input the Item's 13-digit ISBN, Author OR Book Title.\n"
    )

    book_details = isbn_to_details(input_to_isbn())

    """
    If user input is valid,
    Run through book list to find book with same ISBN, author or title.
    Displays details of books and prompts user input for what details to update.
    Also Clears screen for better visibility.
    """

    clear()
    print(
        r"""       
██████╗░░█████╗░░█████╗░██╗░░██╗  ███████╗░█████╗░██╗░░░██╗███╗░░██╗██████╗░██╗
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝  ██╔════╝██╔══██╗██║░░░██║████╗░██║██╔══██╗██║
██████╦╝██║░░██║██║░░██║█████═╝░  █████╗░░██║░░██║██║░░░██║██╔██╗██║██║░░██║██║
██╔══██╗██║░░██║██║░░██║██╔═██╗░  ██╔══╝░░██║░░██║██║░░░██║██║╚████║██║░░██║╚═╝
██████╦╝╚█████╔╝╚█████╔╝██║░╚██╗  ██║░░░░░╚█████╔╝╚██████╔╝██║░╚███║██████╔╝██╗
╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝  ╚═╝░░░░░░╚════╝░░╚═════╝░╚═╝░░╚══╝╚═════╝░╚═╝
"""
    )
    print(
        "\nCongratulations! Your Input is Valid and A Book Has Been Found!\n"
    )

    # gets all books in database
    book_list = get_books()

    # initialize isbn list to check for duplicates when updating books
    isbn_list = []

    for book in book_list:
        # temp variables assigned because we only use this for loop to search for the specific user-inputted book
        (
            temp_isbn,
            temp_author,
            temp_title,
            temp_publisher,
            temp_genre,
            temp_yop,
            temp_dop,
            temp_status,
        ) = book.split("|")

        # adds every book's isbn into isbn_list to check for duplicates
        isbn_list.append(temp_isbn)

        # displays book details

    isbn = book_details[0]
    author = book_details[1]
    title = book_details[2]
    publisher = book_details[3]
    genre = book_details[4]
    yop = book_details[5]
    dop = book_details[6]
    status = book_details[7]

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


    # initialize variables to store old and new details
    old_detail = ""
    new_detail = ""
    detail_type = ""

    user_update_option = input(
        "[1] - ISBN\n[2] - Author\n[3] - Title\n[4] - Publisher\n[5] - Genre\n[6] - Year of Publication\n[7] - Date of Purchase\n[8] - Book Status\n\n"
    )

    if user_update_option not in [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
    ]:
        if user_error_redirect(
            "\nERROR: Invalid Input Detected. Please Input an Option between [1] - [4]."
        ):
            update_book_interface()
        else:
            return 0

    else:
        if user_update_option == "1":
            new_isbn = input("Please Input New ISBN (13 Digits):\n")

            if len(new_isbn) != 13:
                if user_error_redirect(
                    f"\nERROR: ISBN Should Contain EXACTLY 13 digits. Your Input Had {len(new_isbn)} digits."
                ):
                    update_book_interface()
                else:
                    return 0
            else:
                """
                If the user inputted new detail is the same as the old detail. Display message and informs user that no changes will be made.
                The same applies for the other details.
                """

                if new_isbn == isbn:
                    print(
                        f"\nThe New Inputted ISBN is the Same as the Old ISBN. No Changes Will Be Made."
                    )
                else:
                    """
                    If user inputs a new ISBN that already exists in the database,
                    returns an error message and redirects user to input error handling function.
                    """
                    if new_isbn in isbn_list:
                        if user_error_redirect(
                            f"\nERROR: ISBN {new_isbn} Already Exists in Database."
                        ):
                            update_book_interface()
                        else:
                            return 0

                    else:
                        old_detail = isbn
                        new_detail = new_isbn
                        detail_type = "isbn"

        elif user_update_option == "2":
            print(f"Current Author: {author}\n")
            new_author = input("Please Input New Author:\n")
            if new_author == author:
                print(
                    f"\nThe New Inputted Author is the Same as the Old Author. No Changes Will Be Made."
                )
            else:
                old_detail = author
                new_detail = new_author
                detail_type = "author"

        elif user_update_option == "3":
            print(f"Current Title: {title}\n")
            new_title = input("Please Input New Title:\n")

            if new_title == title:
                print(
                    f"\nThe New Inputted Title is the Same as the Old Title. No Changes Will Be Made."
                )

            else:
                old_detail = title
                new_detail = new_title
                detail_type = "title"

        elif user_update_option == "4":
            print(f"Current Publisher: {publisher}\n")
            new_publisher = input("Please Input New Publisher:\n")

            if new_publisher == publisher:
                print(
                    f"\nThe New Inputted Publisher is the Same as the Old Publisher. No Changes Will Be Made."
                )

            else:
                old_detail = publisher
                new_detail = new_publisher
                detail_type = "publisher"

        elif user_update_option == "5":
            print(f"Current Genre: {genre}\n")
            new_genre = input("Please Input New Genre:\n")

            if new_genre == genre:
                print(
                    f"\nThe New Inputted Genre is the Same as the Old Genre. No Changes Will Be Made."
                )

            else:
                old_detail = genre
                new_detail = new_genre
                detail_type = "genre"

        elif user_update_option == "6":
            print(f"Current Year of Publication: {yop}\n")
            new_yop = input("Please Input New Year of Publication:\n")

            if len(new_yop) != 4:
                if user_error_redirect(
                    f"\nERROR: Year of Publication Should Contain EXACTLY 4 digits. Your Input Had {len(new_yop)} digits."
                ):
                    update_book_interface()
                else:
                    return 0

            if new_yop == yop:
                print(
                    f"\nThe New Inputted Year of Publication is the Same as the Old Year of Publication. No Changes Will Be Made."
                )
            else:
                old_detail = yop
                new_detail = new_yop
                detail_type = "yop"

        elif user_update_option == "7":
            print(f"Current Date of Purchase: {dop}\n")
            new_dop = input(
                "Please Input New Date of Purchase (DD/MM/YYYY):\n"
            )

            if len(new_dop) != 10:
                if user_error_redirect(
                    f"\nERROR: Date of Purchase Should Contain EXACTLY 10 characters including '/'. Your Input Had {len(new_dop)} digits."
                ):
                    update_book_interface()
                else:
                    return 0

            dop_day, dop_month, dop_year = new_dop.split("/")

            if int(dop_day) > 31 or int(dop_day) < 1:
                if user_error_redirect(
                    f"\nERROR: Day of Purchase Should Be Between 1 and 31."
                ):
                    update_book_interface()
                else:
                    return 0

            if int(dop_month) > 12 or int(dop_month) < 1:
                if user_error_redirect(
                    f"\nERROR: Month of Purchase Should Be Between 1 and 12."
                ):
                    update_book_interface()
                else:
                    return 0

            if int(dop_year) > 2023 or int(dop_year) < 0:
                if user_error_redirect(
                    f"\nERROR: Year of Purchase Should Be Between 0 and 2023."
                ):
                    update_book_interface()
                else:
                    return 0

            if new_dop == dop:
                print(
                    f"\nThe New Inputted Date of Purchase is the Same as the Old Date of Purchase. No Changes Will Be Made."
                )
            else:
                old_detail = dop
                new_detail = new_dop
                detail_type = "dop"

        elif user_update_option == "8":
            print(f"Current Status: {status}\n")
            new_status = input(
                "Please Input New Status:\n[1] - Wishlist\n[2] - To-Read\n[3] - Reading\n[4] - Completed\n\n"
            )

            if new_status not in ["1", "2", "3", "4"]:
                if user_error_redirect(
                    "\nERROR: Invalid Input Detected. Please Input an Option between [1] - [4]."
                ):
                    update_book_interface()
                else:
                    return 0

            if new_status == "1":
                new_status = "wishlist"
            elif new_status == "2":
                new_status = "to-read"
            elif new_status == "3":
                new_status = "reading"
            else:
                new_status = "completed"

            if new_status == status:
                print(
                    f"\nThe New Inputted Status is the Same as the Old Status. No Changes Will Be Made."
                )

            else:
                old_detail = status
                new_detail = new_status
                detail_type = "status"

    
    if(detail_type == ""):
        print(
            "\nYour Inputted Details are The Same as The Previous Details. Thus, No Changes Will Be Made."
        )
        print(
            "\nNo Updates Will Be Made From Your Input.\nWould You Like to Try Again?\n"
        )
        user_input_option = input("[1] - Yes\n[2] - No\n\n")

        while user_input_option not in ["1", "2"]:
            # error handling: asks user for input again if input is invalid
            print(
                "\nNo Updates Will Be Made From Your Input.\nWould You Like to Try Again?\n"
            )
            user_input_option = input(
                "[1] - Yes, Retry the Function\n[2] - No, Return to Main Menu.\n\n"
            )

        if user_input_option == "1":
            update_book_interface()
        else:
            return 0
        
    else:
        #display book details again
        print("\n______________________________________________________________________________\n")
        print("Update Summary:\n")
        print(f"Old {detail_type.capitalize()}: {old_detail}")
        print(f"New {detail_type.capitalize()}: {new_detail}")

        # double confirms with user to confirm whether they want to update the selected book
        user_option = input(
            "\nAre you sure you want to update this book?\n[1] - Yes\n[2] - No\n"
        )

        # error handling
        if user_option not in ["1", "2"]:
            if user_error_redirect(
                "\nERROR: Invalid Input Detected. Please Input an Option between [1] - [2]."
            ):
                update_book_interface()
            else:
                return 0

        # updates book if user confirms, otherwise returns to main menu
        if user_option == "1":
            update_book(isbn, old_detail, new_detail, detail_type)
        elif user_option == "2":
            print("Okay. The Book will not be Updated.")
            input("Press Any Key to Return to Main Menu.")
            return 0


update_book_interface()

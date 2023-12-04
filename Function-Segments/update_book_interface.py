import os

from get_books import get_books
from user_error_option import user_error_redirect
from update_book import update_book
from check_author_multiple_book import check_author_multiple_book


def clear():
    '''
    Clears the Screen for better visibility.
    '''

    os.system('cls' if os.name == 'nt' else 'clear')


def update_book_interface():
    '''
    Clears the Screen for better visibility.
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

    print("\n\nWelcome to the Book Updating Interface!\n\n")

    print("Displaying All Books in Database...")
    print("Book details have been shortened for readability. In order to view full details, please navigate to display book feature in main menu.")
    print(
        "\nFormat: [Count] | ISBN | Author | Title | Genre | Current Status\n")

    book_count = 0
    book_list = get_books()

    '''
    ISBN, author and title list initialized for user input validation.
    '''
    isbn_list = []
    author_list = []
    title_list = []
    for book in book_list:
        book_count += 1
        isbn, author, title, publisher, genre, yoip, dop, status = book.split(
            "|")
        print(f"[{book_count}] | {isbn} | {
              author} | {title} | {genre} | {status}")

        isbn_list.append(isbn)
        author_list.append(author)
        title_list.append(title)

    print(f"\nAll Books Have Been Displayed.\n")
    print("To Edit an Item, Please Input the Item's 13-digit ISBN, Author OR Book Title.\n")

    user_input_id = input("ISBN / Author / Title:\n")

    '''
    Checks if user inputted digits or text.
    '''

    if (user_input_id.isdigit()):
        '''
        If user attempted to input ISBN but length is not equal to 13, 
        returns an error message as ISBN contains exactly 13 characters.
        '''

        if (len(user_input_id) != 13):
            print(f"\nERROR: ISBN Should Contain EXACTLY 13 digits.\nYour Input Had {
                len(user_input_id)} digits.")
            print("Please Enter a Valid ISBN, Author or Title.")
            if (user_error_redirect()):
                update_book_interface()
            else:
                return 0

        else:
            if (user_input_id not in isbn_list):
                print(f"\nERROR: ISBN {user_input_id} Not Found in Database.")
                if (user_error_redirect()):
                    update_book_interface()
                else:
                    return 0

    else:
        '''
        If user inputted text, 
        Convert text and author and title list to lower-case for better data validation.
        Checks if text input is in author or title list.
        '''
        author_list_lower = [author.lower() for author in author_list]
        title_list_lower = [title.lower() for title in title_list]

        if (user_input_id.lower() not in author_list_lower and user_input_id.lower() not in title_list_lower):
            print(
                f"\nERROR: {user_input_id} Not Found in Database.\nPlease Enter a Valid ISBN, Author or Title.")
            if (user_error_redirect()):
                update_book_interface()
            else:
                return 0

        else:
            '''
            If user input in lower case is in author list or title list,
            convert user input to correct case.
            This is to allow for data validation in the future.
            '''

            if (user_input_id.lower() in author_list_lower):
                user_input_id = author_list[author_list_lower.index(
                    user_input_id.lower())]
            else:
                user_input_id = title_list[title_list_lower.index(
                    user_input_id.lower())]

            ''''
            If user inputted author name,
            Run check_author_multiple_book function to check if author has multiple books in database.
            '''

            if (user_input_id in author_list):
                author_book_list = check_author_multiple_book(user_input_id)

                '''
                Function returns a list of books with same author if author has multiple books.
                Else, function returns False.
                '''

                if (author_book_list):
                    print("\nMultiple Books Found for Author.")
                    print("Please Select the Book to Update:\n")
                    book_count = 0
                    for book in author_book_list:
                        book_count += 1
                        isbn, author, title, publisher, genre, yoip, dop, status = book
                        print(f"[{book_count}] | {isbn} | {title}")

                    print(f"\nTo Update a Book from {
                          user_input_id}, Please Input the Book's 13-digit ISBN or Title from the List.\n")
                    user_input_id = input("ISBN / Title:\n")

                    if (user_input_id.isdigit()):
                        if (len(user_input_id) != 13):
                            print(
                                f"\nERROR: ISBN Should Contain EXACTLY 13 digits.\nYour Input Had {len(user_input_id)} digits.")
                            if (user_error_redirect()):
                                update_book_interface()
                            else:
                                return 0

                        else:
                            if (user_input_id not in isbn_list):
                                print(
                                    f"\nERROR: ISBN {user_input_id} Not Found in Database. Please Enter a Valid ISBN or Title.")
                                if (user_error_redirect()):
                                    update_book_interface()
                                else:
                                    return 0
                    else:
                        if (user_input_id.lower() not in title_list):
                            print(
                                f"\nERROR: {user_input_id} Not Found in Database. Please Enter a Valid ISBN or Title.")
                            if (user_error_redirect()):
                                update_book_interface()
                            else:
                                return 0

    '''
    If user input is valid,
    Run through book list to find book with same ISBN, author or title.
    Displays details of books and prompts user input for what details to update.
    Also Clears screen for better visibility.
    '''

    clear()
    for book in book_list:
        isbn, author, title, publisher, genre, yoip, dop, status = book.split(
            "|")
        if (isbn == user_input_id or author == user_input_id or title == user_input_id):
            print(f"\nBook Found: {title} by {author}")
            print("Book Details:\n")
            print(f"ISBN: {isbn}")
            print(f"Author: {author}")
            print(f"Title: {title}")
            print(f"Publisher: {publisher}")
            print(f"Genre: {genre}")
            print(f"Year of Initial Publication: {yoip}")
            print(f"Date of Latest Publication: {dop}")
            print(f"Status: {status}")

            print("What Details Would You Like to Update?\n")
            user_update_option = input(
                "[1] - ISBN\n[2] - Author\n[3] - Title\n[4] - Publisher\n[5] - Genre\n[6] - Year of Initial Publication\n[7] - Date of Latest Publication\n[8] - Book Status\n\n")

            if (user_update_option not in ['1', '2', '3', '4', '5', '6', '7', '8']):
                print(
                    "\nERROR: Invalid Input Detected. Please Input an Option between [1] - [4].")
                if (user_error_redirect()):
                    update_book_interface()
                else:
                    return 0

            else:
                if (user_update_option == '1'):
                    new_isbn = input(
                        "Please Input New ISBN (13 Digits):\n")

                    if (len(new_isbn) != 13):
                        print(
                            f"\nERROR: ISBN Should Contain EXACTLY 13 digits.\nYour Input Had {len(new_isbn)} digits.")
                        if (user_error_redirect()):
                            update_book_interface()
                        else:
                            return 0
                    else:
                        if (new_isbn in isbn_list):
                            print(
                                f"\nERROR: ISBN {new_isbn} Already Exists in Database.")
                            if (user_error_redirect()):
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
                        f"Current Year of Initial Publication: {yoip}\n")
                    new_yoip = input(
                        "Please Input New Year of Initial Publication:\n")
                    update_book(
                        yoip, new_yoip, "yoip")

                elif (user_update_option == '7'):
                    print(
                        f"Current Date of Latest Publication: {dop}\n")
                    new_dop = input(
                        "Please Input New Date of Latest Publication:\n")
                    update_book(
                        dop, new_dop, "dop")

                elif (user_update_option == '8'):
                    print(
                        f"Current Status: {status}\n")
                    new_status = input(
                        "Please Input New Status:\n[1] - Wishlist\n[2] - To-Read\n[3] - Reading\n[4] - Completed\n\n")

                    if (new_status not in ["1", "2", "3", "4"]):
                        print(
                            "\nERROR: Invalid Input Detected. Please Input an Option between [1] - [4].")
                        if (user_error_redirect()):
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

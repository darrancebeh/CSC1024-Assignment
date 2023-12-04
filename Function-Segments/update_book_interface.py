import os

from get_books import get_books
from user_error_option import user_error_redirect
from update_book import update_book


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
        isbn, author, title, publisher, genre, dow, dop, status = book.split(
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
                for book in book_list:
                    isbn, author, title, publisher, genre, yoip, dop, status = book.split(
                        "|")
                    if (isbn == user_input_id):
                        print(f"\nBook Found: {title} by {author}")
                        print("Book Details:\n")
                        print(f"Publisher: {publisher}")
                        print(f"Genre: {genre}")
                        print(f"Year of Initial Publication: {yoip}")
                        print(f"Date of Latest Publication: {dop}")
                        print(f"Status: {status}")

                        print("What Details Would You Like to Update?\n")
                        user_update_option = int(input(
                            "[1] - ISBN\n[2] - Author\n[3] - Title\n[4] - Publisher\n[5] - Genre\n[6] - Year of Initial Publication\n[7] - Date of Latest Publication\n[8] - Book Status\n\n"))
                        if (user_update_option not in range(1, 9)):
                            print(
                                "\nERROR: Invalid Input Detected. Please Input an Option between [1] - [8].")
                            if (user_error_redirect()):
                                update_book_interface()
                            else:
                                return 0

                        else:
                            if (user_update_option == 1):
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
                                            isbn, new_isbn, book_list)


update_book_interface()

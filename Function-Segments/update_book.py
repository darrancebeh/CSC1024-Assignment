import os

from get_books import get_books
from user_error_option import user_error_redirect


def clear():
    '''
    Clears the Screen for better visibility.
    '''

    os.system('cls' if os.name == 'nt' else 'clear')


def update_book():
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
    for book in book_list:
        book_count += 1
        isbn, author, title, publisher, genre, dow, dop, status = book.split(
            "|")
        print(f"[{book_count}] | {isbn} | {
              author} | {title} | {genre} | {status}")

    print(f"\nAll Books Have Been Displayed.\n")
    print("To Edit an Item, Please Input the Item's 13-digit ISBN, Author OR Book Title.\n")

    user_input_id = input("ISBN / Author / Title:\n")

    '''
    Checks if user inputted digits or text.
    '''

    if (user_input_id.isdigit()):
        '''
        If user attempted to input ISBN but length is not equal to 13, returns an error message as ISBN contains exactly 13 characters.
        '''

        if (len(user_input_id) != 13):
            print(f"\nERROR: ISBN Should Contain EXACTLY 13 digits.\nYour Input Had {
                  len(user_input_id)} digits.")
            if (user_error_redirect()):
                update_book()
            else:
                return 0


update_book()

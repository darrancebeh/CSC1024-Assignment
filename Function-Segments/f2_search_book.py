from aux1_get_books import get_books
from aux3_user_error_option import user_error_redirect
from aux4_input_to_isbn import input_to_isbn
from f1_display_books import display_books
from aux5_isbn_to_details import isbn_to_details


def search_books():
    '''
    Prompts user to input ISBN, name of author and/or title.
    Displays header for the function.
    '''
    print(r"""

░██████╗███████╗░█████╗░██████╗░░█████╗░██╗░░██╗  ██████╗░░█████╗░░█████╗░██╗░░██╗
██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██║░░██║  ██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
╚█████╗░█████╗░░███████║██████╔╝██║░░╚═╝███████║  ██████╦╝██║░░██║██║░░██║█████═╝░
░╚═══██╗██╔══╝░░██╔══██║██╔══██╗██║░░██╗██╔══██║  ██╔══██╗██║░░██║██║░░██║██╔═██╗░
██████╔╝███████╗██║░░██║██║░░██║╚█████╔╝██║░░██║  ██████╦╝╚█████╔╝╚█████╔╝██║░╚██╗
╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝  ╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝

░█████╗░░█████╗░████████╗░█████╗░██╗░░░░░░█████╗░░██████╗░██╗░░░██╗███████╗
██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██║░░░░░██╔══██╗██╔════╝░██║░░░██║██╔════╝
██║░░╚═╝███████║░░░██║░░░███████║██║░░░░░██║░░██║██║░░██╗░██║░░░██║█████╗░░
██║░░██╗██╔══██║░░░██║░░░██╔══██║██║░░░░░██║░░██║██║░░╚██╗██║░░░██║██╔══╝░░
╚█████╔╝██║░░██║░░░██║░░░██║░░██║███████╗╚█████╔╝╚██████╔╝╚██████╔╝███████╗
░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░░╚═════╝░╚══════╝""")

    book_list = get_books()
    display_books()

    print("___________________________________________\n")

    book_details = isbn_to_details(input_to_isbn())

    print("Displaying Searched Book Details...\n")

    print(f"\nBook Found: {book_details[2]} by {book_details[1]}\n")
    print(f"ISBN      : {book_details[0]}")
    print(f"Author    : {book_details[1]}")
    print(f"Title     : {book_details[2]}")
    print(f"Publisher : {book_details[3]}")
    print(f"Genre     : {book_details[4]}")
    print(f"Year of Publication : {book_details[5]}")
    print(f"Date of Purchase    : {book_details[6]}")
    print(f"Status: {book_details[7]}")


search_books()

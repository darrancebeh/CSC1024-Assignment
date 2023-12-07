from get_books import get_books
from user_error_option import user_error_redirect

'''
List to store books that match user input.
'''
matching_books = []
'''
Assign get_books function to book_list variable.
'''
book_list = get_books()

'''
Function that displays each result if the matching_books list is not empty.
Otherwise, it displays that no matching books were found.
'''


def display_matching_books(matching_books):
    '''
    Check if the matching_books list is not empty, then display each result.
    Displays header when book is found.
    '''
    if matching_books:
        print(r"""       
██████╗░░█████╗░░█████╗░██╗░░██╗  ███████╗░█████╗░██╗░░░██╗███╗░░██╗██████╗░██╗
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝  ██╔════╝██╔══██╗██║░░░██║████╗░██║██╔══██╗██║
██████╦╝██║░░██║██║░░██║█████═╝░  █████╗░░██║░░██║██║░░░██║██╔██╗██║██║░░██║██║
██╔══██╗██║░░██║██║░░██║██╔═██╗░  ██╔══╝░░██║░░██║██║░░░██║██║╚████║██║░░██║╚═╝
██████╦╝╚█████╔╝╚█████╔╝██║░╚██╗  ██║░░░░░╚█████╔╝╚██████╔╝██║░╚███║██████╔╝██╗
╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝  ╚═╝░░░░░░╚════╝░░╚═════╝░╚═╝░░╚══╝╚═════╝░╚═╝""")

        '''
        Run the if statement when there is only 1 book that matches the input.
        Otherwise run the elif statement if multiple books match the input.
        Present the book in a user-friendly order.
        '''

        if len(matching_books) == 1:
            print(f"\n 1 book matches the details you entered:")
        elif len(matching_books) > 1:
            print(f"\n{len(matching_books)} books match the details you entered:")
        for book in matching_books:
            print(f"\nBook Found: {book[2]} by {book[1]}")
            print("Book Details:\n")
            print(f"ISBN: {book[0]}")
            print(f"Author: {book[1]}")
            print(f"Title: {book[2]}")
            print(f"Publisher: {book[3]}")
            print(f"Genre: {book[4]}")
            print(f"Year of Publication: {book[5]}")
            print(f"Date of Purchase: {book[6]}")
            print(f"Status: {book[7]}")

    else:
        print("\nNo matching books found.\n")
    '''
    If no matching books were found, display a message.
    '''


'''
Function to allow the user to search for a book by ISBN, author, and/or title.
It iterates through the book list and compiles matching books based on user input.
Displays the results and handles ISBN-related errors.
'''


def search_books(book_list):
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

    print("\n\nTo find your desired book, please provide some details below.\n")

    isbn = input("Enter ISBN (or leave blank): ")
    author = input("Enter name of author (or leave blank): ").lower()
    title = input("Enter book title (or leave blank): ").lower()

    '''
    Checks if there is an ISBN, author, or title input; then checks if it matches with any books in the database.
    Assign variable names such as isbn_match for clarity.
    if input matches with any book, append to the matching_books list.
    '''
    for book in book_list:
        book = book.split("|")
        isbn_match = isbn and isbn in book[0]
        author_match = author and author in book[1].lower()
        title_match = title and title in book[2].lower()

        if isbn_match or author_match or title_match:
            matching_books.append(book)

    '''
    Runs the display_matching_books function after matching_books list has been compiled.
    '''
    display_matching_books(matching_books)

    '''
    Section that handles checks and errors.
    '''
    if (isbn.isdigit()):
        '''
        runs if isbn is a digit string.
        '''
        if ((len(isbn)) != 13):
            '''
            runs if length of the ISBN string is NOT 13.
            '''
            if (user_error_redirect(f"\nERROR: ISBN Should Contain EXACTLY 13 digits. Your Input Had {len(isbn)} digits.")):
                search_books(book_list)
            else:
                return 0

    if (author.isdigit()):
        '''
        Checks for any numbers in author input
        '''
        if (user_error_redirect(f"\nERROR: Author name must not include any digits.")):
            search_books(book_list)
        else:
            return 0

    if (title.isdigit()):
        '''
        Checks for any numbers in title input
        '''
        if (user_error_redirect(f"\nERROR: Title must not include any digits.")):
            search_books(book_list)
        else:
            return 0


search_books(book_list)

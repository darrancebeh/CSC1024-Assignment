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
    '''
    if matching_books:
        print("Matching books found:")
        for book in matching_books:
            print(book)

    else:
        print("No matching books found.")
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
    '''
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
    Section that handles ISBN-related checks and errors.
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


search_books(book_list)

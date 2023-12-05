from get_books import get_books

# ! DARRANCE !
# in the assignment details, it says:
#
# Data from books_StudentID.txt must be read and stored in the program when the program first runs
# so that all the book information previously stored in the text file will be displayed
# if it is the first option selected when starting the program.
#
# so I'm not sure if we need to do some kind of open() function at the start of the program?


def display_books():  # add headings for columns!!!
    '''
    Displays header.
    '''

    print(r'''
░█████╗░██╗░░░░░██╗░░░░░  ██████╗░░█████╗░░█████╗░██╗░░██╗░██████╗
██╔══██╗██║░░░░░██║░░░░░  ██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝
███████║██║░░░░░██║░░░░░  ██████╦╝██║░░██║██║░░██║█████═╝░╚█████╗░
██╔══██║██║░░░░░██║░░░░░  ██╔══██╗██║░░██║██║░░██║██╔═██╗░░╚═══██╗
██║░░██║███████╗███████╗  ██████╦╝╚█████╔╝╚█████╔╝██║░╚██╗██████╔╝
╚═╝░░╚═╝╚══════╝╚══════╝  ╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░''')

    '''
    The book list is split into individual books.
    The individual books are further split into their details.

    The longest column length (the length of the longest detail in the column) is determined.
    Then, the detail is printed in a space that is the longest column length + 2 characters.
    This is done for every detail of the book.

    A newline is created to separate each book, and the process repeats for each book.
    '''

    book_list = get_books()

    for book in book_list:
        book_details = book.split("|")

        for detail in book_details:
            column_length = get_max_column_length(
                book_details.index(detail)) + 2
            # +2 to leave a little space before the next column and prevent them from being too close together.

            print(f"{detail: <{column_length}}", end="")

        print("\n")


def get_max_column_length(column):
    '''
    Function to get the longest column length of the specified detail column.
    This will help to ensure that the displayed columns will not be too short nor too long even if the details are lengthened.
    '''

    '''
    Makes an empty list of the lengths of all the items in the specified detail column.
    '''

    column_lengths = []

    '''
    The book list is split into individual books.
    The length of the specified detail for each book is put into the list.

    eg: column = 1 refers to the 'author' column.
        The length of 'Yasha Levine' is 12.
        12 is added into the list.
        This is done for every book.
    '''

    book_list = get_books()

    for book in book_list:
        book_details = book.split("|")

        column_lengths.append(len(book_details[column]))

    '''
    Finds the largest number in the list of column lengths and returns it.
    '''

    max_column_length = max(column_lengths)
    return max_column_length


display_books()

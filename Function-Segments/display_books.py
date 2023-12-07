from get_books import get_books


def display_books():
    '''
    Displays header.
    '''

    print(r'''
░█████╗░██╗░░░░░██╗░░░░░  ██████╗░░█████╗░░█████╗░██╗░░██╗░██████╗
██╔══██╗██║░░░░░██║░░░░░  ██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝
███████║██║░░░░░██║░░░░░  ██████╦╝██║░░██║██║░░██║█████═╝░╚█████╗░
██╔══██║██║░░░░░██║░░░░░  ██╔══██╗██║░░██║██║░░██║██╔═██╗░░╚═══██╗
██║░░██║███████╗███████╗  ██████╦╝╚█████╔╝╚█████╔╝██║░╚██╗██████╔╝
╚═╝░░╚═╝╚══════╝╚══════╝  ╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░
          
          ''')

    '''
    Creates the list of categories
    '''
    categories = ["ISBN", "AUTHOR", "TITLE", "PUBLISHER",
                  "GENRE", "YEAR PUBLISHED", "DATE PURCHASED", "STATUS"]

    '''
    The longest column length (the length of the longest detail in the column) is determined.
    If the name of the category is longer than the longest column length, the column is widened to its length.
    Prints the name of the category.

    This is done for every category.
    '''

    for category in categories:

        column_length = get_max_column_length(categories.index(category)) + 2
        # +3 to leave a little space before the next column and prevent them from being too close together.

        if column_length < len(category):
            column_length = len(category) + 2

        print(f"{category: <{column_length}}", end="")

    print("\n")

    '''
    The book list is split into individual books.
    The individual books are further split into their details.

    The longest column length (the length of the longest detail in the column) is determined.
    If the name of the category is longer than the longest column length, the column is widened to its length.

    Then, the detail is printed in a consistently-sized space.
    This is done for every detail of the book.

    A newline is created to separate each book, and the process repeats for each book.
    '''

    book_list = get_books()

    for book in book_list:

        book_details = book.split("|")

        for detail in book_details:

            column_length = get_max_column_length(
                book_details.index(detail)) + 2
            # +3 to leave a little space before the next column and prevent them from being too close together.

            if column_length < len(categories[book_details.index(detail)]):
                column_length = len(categories[book_details.index(detail)]) + 2

            print(f"{detail: <{column_length}}", end="")

        print("\n")


def get_max_column_length(category):
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

        column_lengths.append(len(book_details[category]))

    '''
    Finds the largest number in the list of column lengths and returns it.
    '''

    max_column_length = max(column_lengths)
    return max_column_length

#
#
#
#
########## Work in (a lot of) progress ##########


def make_each_book_into_a_list():  # should probably change the function name
    '''
    The book list is split into individual books.
    '''

    book_list = get_books()
    book_list_of_multiple_lists = []

    for book in book_list:

        book_details = book.split("|")
        book_list_of_multiple_lists.append(book_details)

    return book_list_of_multiple_lists


def sort_books(category, order):
    book_list_of_multiple_lists = make_each_book_into_a_list()
    sorted_list = sorted(book_list_of_multiple_lists,
                         key=lambda x: x[category], reverse=order)
    return sorted_list


def turn_into_single_list(list_with_lists):

    single_list = []

    for book_as_list in list_with_lists:

        single_book = "|".join(book_as_list)

        single_list.append(single_book)

    return single_list


def display_sorted_books(single_sorted_list):
    '''
    Displays header.
    '''

    print(r'''
░█████╗░██╗░░░░░██╗░░░░░  ██████╗░░█████╗░░█████╗░██╗░░██╗░██████╗
██╔══██╗██║░░░░░██║░░░░░  ██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝
███████║██║░░░░░██║░░░░░  ██████╦╝██║░░██║██║░░██║█████═╝░╚█████╗░
██╔══██║██║░░░░░██║░░░░░  ██╔══██╗██║░░██║██║░░██║██╔═██╗░░╚═══██╗
██║░░██║███████╗███████╗  ██████╦╝╚█████╔╝╚█████╔╝██║░╚██╗██████╔╝
╚═╝░░╚═╝╚══════╝╚══════╝  ╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░
          
          ''')

    '''
    Creates the list of categories
    '''
    categories = ["ISBN", "AUTHOR", "TITLE", "PUBLISHER",
                  "GENRE", "YEAR PUBLISHED", "DATE PURCHASED", "STATUS"]

    '''
    The longest column length (the length of the longest detail in the column) is determined.
    If the name of the category is longer than the longest column length, the column is widened to its length.
    Prints the name of the category.

    This is done for every category.
    '''

    for category in categories:

        column_length = get_max_column_length(categories.index(category)) + 2
        # +3 to leave a little space before the next column and prevent them from being too close together.

        if column_length < len(category):
            column_length = len(category) + 2

        print(f"{category: <{column_length}}", end="")

    print("\n")

    '''
    The book list is split into individual books.
    The individual books are further split into their details.

    The longest column length (the length of the longest detail in the column) is determined.
    If the name of the category is longer than the longest column length, the column is widened to its length.

    Then, the detail is printed in a consistently-sized space.
    This is done for every detail of the book.

    A newline is created to separate each book, and the process repeats for each book.
    '''

    book_list = single_sorted_list

    for book in book_list:

        book_details = book.split("|")

        for detail in book_details:

            column_length = get_max_column_length(
                book_details.index(detail)) + 2
            # +3 to leave a little space before the next column and prevent them from being too close together.

            if column_length < len(categories[book_details.index(detail)]):
                column_length = len(categories[book_details.index(detail)]) + 2

            print(f"{detail: <{column_length}}", end="")

        print("\n")


'''
↓ MAIN INTERACTABLE-ISH CODE ↓
'''

display_books()

already_sorted = 0

# CANNOT handle input errors at all yet
# Also unknown what will happen if there are duplicate copies but different date purchased/status
while already_sorted == 0:

    if input("Sort the display? (Enter N to decline or anything else to accept) \n").upper() == "N":
        break

    category_input = int(input(r'''
Sort by:
ISBN [1]
Author [2]
Title [3]
Publisher [4]
Genre [5]
Year Published [6]
Date Purchased [7]
Status [8]
'''))

    order_input = int(input(r'''          
Ascending order (A→Z/0→9) [1]
Descending order (Z→A/9→0) [2]
'''))

    category = category_input - 1  # from 0-7
    order = order_input - 1  # from 0-1 (True/False)

    sorted_list = sort_books(category, order)
    single_sorted_list = turn_into_single_list(sorted_list)
    display_sorted_books(single_sorted_list)

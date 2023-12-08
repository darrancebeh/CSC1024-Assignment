from aux1_get_books import get_books
from f1_display_books import get_max_column_length

# This whole sorting function is meant to be called after display_books()


########## Work in (a lot of) progress ##########
# REMEMBER to put proper documentation later
#


def make_each_book_into_a_sublist():  # should probably change the function name
    '''
    The book list is split into individual books.
    '''

    book_list = get_books()
    list_with_books_as_sublists = []

    for book in book_list:

        book_details = book.split("|")
        list_with_books_as_sublists.append(book_details)

    return list_with_books_as_sublists


def sort_books(category, order):

    list_with_books_as_sublists = make_each_book_into_a_sublist()

    '''
    Sorts the big list of books according to arguments 'category' and 'order'.
    '''
    sorted_list = sorted(list_with_books_as_sublists,
                         key=lambda x: x[category], reverse=order)
    '''
    Returns the sorted list.
    '''
    return sorted_list


def turn_into_single_list(sorted_list):
    '''
    Makes empty list named single_list.
    '''
    single_list = []

    '''
    For every book in the sorted list, the book details are joined together, transforming from a sublist of details into one element of details separated by "|".
        ie: [["9781668026038","Hannah Grace",...]["9780063052734","Danya Kukafka",...]]
            turns into
            ["9781668026038|Hannah Grace|...","9780063052734|Danya Kukafka|..."]

    '''
    for book_as_sublist in sorted_list:

        book = "|".join(book_as_sublist)

        single_list.append(book)

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


def sort_books():
    # CANNOT handle input errors at all yet
    # Also unknown what will happen if there are duplicate copies but different date purchased/status
    while True:

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

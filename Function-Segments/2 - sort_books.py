from aux1_get_books import get_books
from f1_display_books import get_max_column_length

# This whole sorting function is meant to be called after display_books().
# Seems like uncapitalised author names are sorted as last when sorted in ascending order, and vice versa.


def turn_books_into_sublists():
    '''
    The book list is split into individual books.
    An empty list 'book_superlist' is created to store the books as sublists.
    '''

    book_list = get_books()
    book_superlist = []

    '''
    For every book in the unsorted list, the details in the form of a single element are separated into individual elements in a sublist.
        ie: "9781668026038|Hannah Grace|..."
            turns into:
            ["9781668026038","Hannah Grace",...]

    The book, now in sublist form, is appended to 'book_superlist'.
    This is done for every book.
        ie: []
            turns into:
            [["9781668026038","Hannah Grace",...]]
            then:
            [["9781668026038","Hannah Grace",...],["9780063052734","Danya Kukafka",...]]
            and so on.
    '''

    for book in book_list:

        book_details = book.split("|")

        book_superlist.append(book_details)

    '''
    Returns the book list consisting of only sublists and no elements.
    '''

    return book_superlist


def sort_book_superlist(category, order):
    '''
    Gets superlist of books in sublist form.
    '''
    book_superlist = turn_books_into_sublists()

    '''
    Sorts the superlist of books according to arguments 'category' and 'order'.
    '''
    sorted_superlist = sorted(book_superlist,
                              key=lambda x: x[category], reverse=order)
    '''
    Returns the sorted list.
    '''
    return sorted_superlist


def turn_superlist_into_single_list(sorted_superlist):
    '''
    Makes empty list named single_list to store all the books as elements.
    '''
    single_list = []

    '''
    For every book in the sorted list, the book details are joined together, transforming from a sublist of details into one element of details separated by '|'.
        ie: ["9781668026038","Hannah Grace",...]
            turns into:
            "9781668026038|Hannah Grace|..."

    The book, now in element form, is appended to 'single_list'.
    This is done for every book.
        ie: []
            turns into:
            ["9781668026038|Hannah Grace|..."]
            then:
            ["9781668026038|Hannah Grace|...","9780063052734|Danya Kukafka|..."]
            and so on.
    '''
    for book_as_sublist in sorted_superlist:

        book = "|".join(book_as_sublist)

        single_list.append(book)

    '''
    Returns the book list consisting of only elements and no sublists.
    '''

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


def input_check(inp, accepted_range):
    '''
    Checks if inp is in accepted_range.
    If yes, returns ok = 1.
    If not, returns ok = 0.
    '''
    if inp in accepted_range:
        ok = 1

    else:
        ok = 0

    return ok


def ask_sort_books():
    '''
    Loop to repeatedly ask user if they want to sort the display of books.

    If 'n' or 'N' is entered, breaks the loop.
    If anything else is entered, continues on with sorting options.
    '''
    while True:

        if input("-----------------------------------------------------------------\nSort the display? (Enter N to decline or anything else to accept) \n").upper() == "N":
            break

        '''
        Checks if input is an integer.
        If not, prints "Error, please try again."
        '''

        try:

            category_input = int(input(r'''
Sort by:
ISBN [1]
Author [2]
Title [3]
Publisher [4]
Genre [5]
Year Published [6]
Status [7]
'''))

        except:

            print("Error, please try again.")

        else:

            '''
            Checks if input is an element in the list [1, 2, 3, 4, 5, 6, 7].
            If not, prints "Error: not an available option."
            '''
            ok = input_check(category_input, [1, 2, 3, 4, 5, 6, 7])

            if ok == 0:
                print("Error: not an available option.")

            else:

                '''
                If 'category_input' is from 1 to 6, sets variable 'category' to 'category_input' minus 1.
                This is done in order to match with the indexes of the categories.

                eg: The index of ISBN in a book sublist is 0. 'category_input' is 1. 'category' = 0.
                    Later on, in the function sort_book_superlist(category, order), category is set to 0, referring to the ISBN detail.

                Here, 'category' only goes from 0 to 5.
                '''
                if category_input <= 6:
                    category = category_input - 1

                    '''
                If 'category_input' is 7, sets variable 'category' to 7.

                The index of Status in a book sublist is 7. 
                The index of Date Purchased, 6, is skipped because it cannot be sorted properly.
                    '''

                elif category_input == 7:
                    category = 7

                '''
                Checks if input is an integer.
                If not, prints "Error, please try again."
                '''
                try:

                    order_input = int(input(r'''          
Ascending order (A→Z/0→9) [1]
Descending order (Z→A/9→0) [2]
'''))

                except:

                    print("Error, please try again.")

                else:

                    '''
                    Checks if input is an element in the list [1, 2].
                    If not, prints "Error: not an available option."
                    '''
                    ok = input_check(order_input, [1, 2])

                    if ok == 0:
                        print("Error: not an available option.")

                    else:
                        '''
                        'order' is set to 'order_input' minus 1 in order to match with 0 and 1.
                        This is done to decide if the list should be sorted in the ascending or descending order in the sort_book_superlist(category, order) function.
                        0 = ascending order, because reverse=0.
                        1 = descending order, because reverse=1.
                        '''
                        order = order_input - 1

                        '''
                        The book superlist is created and sorted according to the user-selected category and order.
                        The book superlist is turned into a single list with books as elements.
                        The sorted book list is displayed.
                        '''
                        sorted_superlist = sort_book_superlist(category, order)
                        single_sorted_list = turn_superlist_into_single_list(
                            sorted_superlist)
                        display_sorted_books(single_sorted_list)

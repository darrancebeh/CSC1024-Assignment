import os

from aux1_get_books import get_books


def clear():
    """
    Clears the Screen for better visibility.
    """

    os.system("cls" if os.name == "nt" else "clear")


def display_books():
    """
    Calls the clear function to clear the screen for better visiblity.
    Displays header for the function. (All Books)
    """

    clear()

    print(
        r"""
░█████╗░██╗░░░░░██╗░░░░░  ██████╗░░█████╗░░█████╗░██╗░░██╗░██████╗
██╔══██╗██║░░░░░██║░░░░░  ██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝
███████║██║░░░░░██║░░░░░  ██████╦╝██║░░██║██║░░██║█████═╝░╚█████╗░
██╔══██║██║░░░░░██║░░░░░  ██╔══██╗██║░░██║██║░░██║██╔═██╗░░╚═══██╗
██║░░██║███████╗███████╗  ██████╦╝╚█████╔╝╚█████╔╝██║░╚██╗██████╔╝
╚═╝░░╚═╝╚══════╝╚══════╝  ╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░
          
          """
    )

    """
    Creates the list of categories
    """
    categories = [
        "ISBN",
        "AUTHOR",
        "TITLE",
        "PUBLISHER",
        "GENRE",
        "YEAR PUBLISHED",
        "DATE PURCHASED",
        "STATUS",
    ]

    """
    The longest column length (the length of the longest detail in the column) is determined.
    If the name of the category is longer than the longest column length, the column is widened to its length.
    Prints the name of the category.

    This is done for every category.
    """

    for category in categories:
        column_length = get_max_column_length(categories.index(category)) + 2
        # +2 to leave a little space before the next column and prevent them from being too close together.

        if column_length < len(category):
            column_length = len(category) + 2

        print(f"{category: <{column_length}}", end="")

    print("\n")

    """
    The book list is split into individual books.
    The individual books are further split into their details.

    The longest column length (the length of the longest detail in the column) is determined.
    If the name of the category is longer than the longest column length, the column is widened to its length.

    Then, the detail is printed in a consistently-sized space.
    This is done for every detail of the book.

    A newline is created to separate each book, and the process repeats for each book.
    """

    book_list = get_books()

    for book in book_list:
        book_details = book.split("|")

        for detail in book_details:
            column_length = (
                get_max_column_length(book_details.index(detail)) + 2
            )
            # +2 to leave a little space before the next column and prevent them from being too close together.

            if column_length < len(categories[book_details.index(detail)]):
                column_length = len(categories[book_details.index(detail)]) + 2

            print(f"{detail: <{column_length}}", end="")

        print("\n")


def get_max_column_length(category):
    """
    Function to get the longest column length of the specified detail column.
    This will help to ensure that the displayed columns will not be too short nor too long even if the details are lengthened.
    """

    """
    Makes an empty list of the lengths of all the items in the specified detail column.
    """

    column_lengths = []

    """
    The book list is split into individual books.
    The length of the specified detail for each book is put into the list.

    eg: column = 1 refers to the 'author' column.
        The length of 'Yasha Levine' is 12.
        12 is added into the list.
        This is done for every book.
    """

    book_list = get_books()

    for book in book_list:
        book_details = book.split("|")

        column_lengths.append(len(book_details[category]))

    """
    Finds the largest number in the list of column lengths and returns it.
    """

    max_column_length = max(column_lengths)
    return max_column_length


display_books()

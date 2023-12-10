import os
from datetime import datetime
# import os for terminal screen clearing
# import datetime for date and time functions for user experience improvement

'''
Auxilary Functions START
'''

# function to clear terminal screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# function to get all books and details in database
def get_books():
    """
    Returns a list of all books in the database.
    """

    with open("books_23094907.txt", "r") as f:
        """
        Returns all lines contained in the text file and separates every list item by line.
        """
        book_list = f.read().split("\n")
        return book_list


# function to check if an author has multiple books in database
def check_author_multiple_book(author):
    """
    Given author name, checks if author has multiple books in database.
    If author has multiple books, return list of all books of author.
    Else, return False.
    """
    book_list = get_books()
    author_book_list = []
    for book in book_list:
        book_details = book.split("|")
        if book_details[1] == author:
            author_book_list.append(book_details)

    if len(author_book_list) > 1:
        return author_book_list
    else:
        return False

def user_error_redirect(message):
    """
    Clears screen for visibility and displays error header.
    """
    clear()
    print(
        r"""
███████╗██████╗░██████╗░░█████╗░██████╗░  ░█████╗░░█████╗░░█████╗░██╗░░░██╗██████╗░██████╗░███████╗██████╗░██╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔══██╗██╔══██╗██╔══██╗██║░░░██║██╔══██╗██╔══██╗██╔════╝██╔══██╗██║
█████╗░░██████╔╝██████╔╝██║░░██║██████╔╝  ██║░░██║██║░░╚═╝██║░░╚═╝██║░░░██║██████╔╝██████╔╝█████╗░░██║░░██║██║
██╔══╝░░██╔══██╗██╔══██╗██║░░██║██╔══██╗  ██║░░██║██║░░██╗██║░░██╗██║░░░██║██╔══██╗██╔══██╗██╔══╝░░██║░░██║╚═╝
███████╗██║░░██║██║░░██║╚█████╔╝██║░░██║  ╚█████╔╝╚█████╔╝╚█████╔╝╚██████╔╝██║░░██║██║░░██║███████╗██████╔╝██╗
╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝  ░╚════╝░░╚════╝░░╚════╝░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝"""
    )

    print("\nOh No! Looks Like You Inputted Something Wrong!\n")
    print(f"Error Encountered: {message}\n")
    print("Please Read Prompt Instructions Carefully and Try Again!\n")

    """
    Function to let user decide whether to retry input upon error or redirect to main menu.
    """

    user_input_option = input(
        "\nRetry Input?\n[1] - Retry Input.\n[2] - Back to Main Menu.\n"
    )

    """
    Ensures that user input is either 1 or 2.
    """

    while user_input_option != "1" and user_input_option != "2":
        print("\nInvalid Input Detected. Please Try Again.")
        user_input_option = input(
            "Retry Input?\n[1] - Retry Input.\n[2] - Back to Main Menu.\n"
        )

    """
    Returns True if user decides to retry input.
    Returns False if user decides to return to main menu.
    """

    if user_input_option == "1":
        return True
    else:
        return False
    
def input_to_isbn():
    """
    Gets all books in database.
    """
    book_list = get_books()
    """
    ISBN, author and title list initialized for user input validation.
    """

    isbn_list = []
    author_list = []
    title_list = []

    for book in book_list:
        (
            isbn,
            author,
            title,
            publisher,
            genre,
            yop,
            dop,
            status,
        ) = book.split("|")

        isbn_list.append(isbn)
        author_list.append(author)
        title_list.append(title)

    user_input_id = input("Please Input Book ISBN / Author / Title:\n")

    """
    Checks if user inputted digits or text.
    """

    if user_input_id.isdigit():
        """
        If user attempted to input ISBN but length is not equal to 13,
        returns an error message as ISBN contains exactly 13 characters.
        """

        if len(user_input_id) != 13:
            """
            Redirects user to retry input or return to main menu.
            """

            if user_error_redirect(
                f"\nERROR: ISBN Should Contain EXACTLY 13 digits. Your Input Had {len(user_input_id)} digits."
            ):
                return 1
            else:
                return 0

        else:
            """
            If user inputted ISBN that is not in ISBN list,
            returns an error message and redirects user to input error handling function.
            """

            if user_input_id not in isbn_list:
                if user_error_redirect(
                    f"\nERROR: ISBN {user_input_id} Not Found in Database."
                ):
                    return 1
                else:
                    return 0

    else:
        """
        If user inputted text,
        Convert text and author and title list to lower-case for better data validation.
        Checks if text input is in author or title list.
        """

        author_list_lower = [author.lower() for author in author_list]
        title_list_lower = [title.lower() for title in title_list]

        if (
            user_input_id.lower() not in author_list_lower
            and user_input_id.lower() not in title_list_lower
        ):
            if user_error_redirect(
                f"\nERROR: {user_input_id} Not Found in Database. Please Enter a Valid ISBN, Author or Title."
            ):
                return 1
            else:
                return 0

        else:
            """
            If user input in lower case is in author list or title list,
            convert user input to correct case.
            This is to allow for easier data validation later on.
            """

            if user_input_id.lower() in author_list_lower:
                user_input_id = author_list[
                    author_list_lower.index(user_input_id.lower())
                ]
            else:
                user_input_id = title_list[
                    title_list_lower.index(user_input_id.lower())
                ]

            """'
            If user inputted author name,
            Run check_author_multiple_book function to check if author has multiple books in database.
            """

            if user_input_id in author_list:
                author_book_list = check_author_multiple_book(user_input_id)

                """
                Function returns a list of books with same author if author has multiple books.
                Else, function returns False.
                """

                if author_book_list:
                    print(
                        f"\nMultiple Books Found for Author {user_input_id}."
                    )
                    print("Please Select the Book to Update:\n")
                    book_count = 0

                    """
                    Displays all books under the author's name
                    """

                    for book in author_book_list:
                        book_count += 1
                        (
                            isbn,
                            author,
                            title,
                            publisher,
                            genre,
                            yop,
                            dop,
                            status,
                        ) = book

                        print(
                            f"[{book_count}] | {isbn} | {title} | {genre} | {status}"
                        )

                    """
                    Prompts user to input book number to update.
                    """

                    user_input_book_number = input(
                        f"\nPlease Input Book Number to Update: [1] - [{book_count}]\n"
                    )

                    if user_input_book_number not in [
                        str(i) for i in range(1, book_count + 1)
                    ]:
                        """
                        Data validation to ensure that user input is a valid book number.
                        """

                        if user_error_redirect(
                            f"\nERROR: Invalid Input Detected. Please Input an Option between [1] - [{book_count}]."
                        ):
                            return 1
                        else:
                            return 0
                    else:
                        """
                        If user input is valid,
                        Assigns user inputted book number to associated book ISBN.
                        Filtering books by ISBN makes more sense and is more optimal for data validation.
                        This is because ISBN is unique to each book and WILL NOT HAVE duplicates.
                        """

                        user_input_id = author_book_list[
                            int(user_input_book_number) - 1
                        ][0]

                else:
                    """
                    If no duplicate author-book is found, (meaning that author only has 1 book in database)
                    auto-assign user inputted author name to associated book ISBN.
                    Filtering books by ISBN makes more sense and is more optimal for data validation.
                    This is because ISBN is unique to each book and WILL NOT HAVE duplicates.
                    """

                    """
                    Converts user input to correct author name case.
                    """
                    if user_input_id.lower() in author_list_lower:
                        user_input_id = author_list[
                            author_list_lower.index(user_input_id.lower())
                        ]

                    """
                    Runs through the book list to find book with same author name.
                    Assigns book ISBN to user input.
                    """
                    for book in book_list:
                        (
                            isbn,
                            author,
                            title,
                            publisher,
                            genre,
                            yop,
                            dop,
                            status,
                        ) = book.split("|")
                        if author == user_input_id:
                            user_input_id = isbn

            else:
                """
                If user inputted title,
                Run through book list to find book with same title.
                Assigns book ISBN to user input.
                """

                for book in book_list:
                    (
                        isbn,
                        author,
                        title,
                        publisher,
                        genre,
                        yop,
                        dop,
                        status,
                    ) = book.split("|")
                    if title == user_input_id:
                        user_input_id = isbn

    return user_input_id


def isbn_to_details(isbn):
    """
    Takes in an ISBN and returns the book details.
    """
    book_list = get_books()
    for book in book_list:
        book = book.split("|")
        if isbn == book[0]:
            return book
        

'''
Auxilary Functions END
'''

'''
Utility Functions START
'''

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


def turn_books_into_sublists():
    """
    The book list is split into individual books.
    An empty list 'book_superlist' is created to store the books as sublists.
    """

    book_list = get_books()
    book_superlist = []

    """
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
    """

    for book in book_list:
        book_details = book.split("|")

        book_superlist.append(book_details)

    """
    Returns the book list consisting of only sublists and no elements.
    """

    return book_superlist


def sort_book_superlist(category, order):
    """
    Gets superlist of books in sublist form.
    """
    book_superlist = turn_books_into_sublists()

    """
    Sorts the superlist of books according to 'category' which determines which detail to sort by (using index of detail in book sublist),
    and order, which determines if it will be sorted in ascending or descending order.
    Also takes the lowercase of the chosen detail so that it is sorted properly regardless of letter case.
    """
    sorted_superlist = sorted(
        book_superlist,
        key=lambda book: book[category].lower(),
        reverse=order,
    )
    """
    Returns the sorted list.
    """
    return sorted_superlist


def turn_superlist_into_single_list(sorted_superlist):
    """
    Makes empty list named single_list to store all the books as elements.
    """
    single_list = []

    """
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
    """
    for book_as_sublist in sorted_superlist:
        book = "|".join(book_as_sublist)

        single_list.append(book)

    """
    Returns the book list consisting of only elements and no sublists.
    """

    return single_list


def display_sorted_books(single_sorted_list):
    """
    Displays header.
    """

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

    book_list = single_sorted_list

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


def sort_books():
    """
    Loop to repeatedly ask user if they want to sort the display of books.

    If 'n' or 'N' is entered, breaks the loop.
    If anything else is entered, continues on with sorting options.
    """
    while input(
        "---------------------------------------------------------------------------------------------------\nSort the display? (Enter N to decline and return to main menu, or anything else to accept) \n"
    ).upper() != "N":

        """
        Checks if input is an integer.
        If not, prints "Error, please try again."
        """

        try:
            category_input = int(
                input(
                    r"""
Sort by:
ISBN [1]
Author [2]
Title [3]
Publisher [4]
Genre [5]
Year Published [6]
Status [7]
"""
                )
            )

        except:
            print("Error, please try again.")

        else:

            """
            Checks if input is an element in the list [1, 2, 3, 4, 5, 6, 7].
            If not, prints "Error: not an available option."
            """

            if category_input not in [1, 2, 3, 4, 5, 6, 7]:
                print("Error: not an available option.")

            else:
                """
                If 'category_input' is from 1 to 6, sets variable 'category' to 'category_input' minus 1.
                This is done in order to match with the indexes of the categories.

                eg: The index of ISBN in a book sublist is 0. 'category_input' is 1. 'category' = 0.
                    Later on, in the function sort_book_superlist(category, order), category is set to 0, referring to the ISBN detail.

                Here, 'category' only goes from 0 to 5.
                """
                if category_input <= 6:
                    category = category_input - 1

                    """
                If 'category_input' is 7, sets variable 'category' to 7.

                The index of Status in a book sublist is 7. 
                The index of Date Purchased, 6, is skipped because it cannot be sorted properly.
                    """

                elif category_input == 7:
                    category = 7

                """
                Checks if input is an integer.
                If not, prints "Error, please try again."
                """
                try:
                    order_input = int(
                        input(
                            r"""          
Ascending order (A→Z/0→9) [1]
Descending order (Z→A/9→0) [2]
"""
                        )
                    )

                except:
                    print("Error, please try again.")

                else:

                    """
                    Checks if input is an element in the list [1, 2].
                    If not, prints "Error: not an available option."
                    """

                    if order_input not in [1, 2]:
                        print("Error: not an available option.")

                    else:
                        """
                        'order' is set to 'order_input' minus 1 in order to match with 0 and 1.
                        This is done to decide if the list should be sorted in the ascending or descending order in the sort_book_superlist(category, order) function.
                        1-1 = 0  = ascending order, because reverse=0.
                        2-1 = 1  = descending order, because reverse=1.
                        """
                        order = order_input - 1

                        """
                        The book superlist is created and sorted according to the user-selected category and order.
                        The book superlist is turned into a single list with books as elements.
                        The sorted book list is displayed.
                        """
                        sorted_superlist = sort_book_superlist(category, order)
                        single_sorted_list = turn_superlist_into_single_list(
                            sorted_superlist
                        )
                        display_sorted_books(single_sorted_list)
    
    print("Returning to Main Menu...")
    input("Press Any Key to Continue.")
    return 0


def check_isbn_duplicate(isbn):
    with open("books_23094907.txt", 'r') as f:
        for line in f:
            if line.split('|')[0] == isbn:
                return True
    return False


def add_book_information():
    print("Please enter the following information:")
    while True:
        isbn = input("ISBN number: ")
        if len(isbn) == 13 and isbn.isdigit():
            if check_isbn_duplicate(isbn):
                print("Error. A book with this ISBN already exists.")
                continue
            else:
                break
        else:
            print(
                "Error. ISBN must be 13 digits long and contain only digits. Please try again.")
    while True:
        author = input("Author's name: ")
        if all(word.isalpha() for word in author.split()):
            break
        else:
            print(
                "Error. The author's name must only contain alphabetical characters. Please try again.")
    title = input("Book's title: ")
    publisher = input("Publisher's name: ")
    while True:
        genre = input("Genre of the book: ")
        if all(word.isalpha() for word in genre.split()):
            break
        else:
            print(
                "Error. The genre must only contain alphabetical characters. Please try again.")
    while True:
        published_year = input("Publishing year: ")
        if len(published_year) == 4 and published_year.isdigit() and int(published_year) > 0 and int(published_year) <= datetime.now().year:
            published_date = datetime(int(published_year), 1, 1)
            break
        else:
            print("Error. Publishing year must be a 4-digit positive integer and not in the future. Please try again.")
    while True:
        date_purchased_str = input("Date purchased in the format DD/MM/YYYY: ")
        if len(date_purchased_str) != 10:
            print(
                "Error. The date must be exactly 10 characters long in the format DD/MM/YYYY. Please try again.")
            continue
        try:
            date_purchased = datetime.strptime(date_purchased_str, '%d/%m/%Y')
            if date_purchased <= datetime.now() and date_purchased > published_date:
                break
            else:
                print(
                    "Error. The purchase date must be after the publishing year. Please try again.")
        except ValueError:
            print("Error. The date format is incorrect. Please try again.")
    while True:
        print("Please input the book's status:")
        print("[1] - wishlist")
        print("[2] - to-read")
        print("[3] - reading")
        print("[4] - completed")
        print()
        status_input = input("Book's status (enter a number from 1 to 4): ")
        status_options = {'1': 'wishlist', '2': 'to-read',
                          '3': 'reading', '4': 'completed'}
        if status_input in status_options:
            status = status_options[status_input]
            break
        else:
            print("Error. Invalid status. Please try again.")

    return isbn, author, title, publisher, genre, published_year, date_purchased_str, status


'''
Utility Functions END
'''

'''
Main Program Functional Requirements START
'''

#Functional Requirement 1 - Display Book Record(s)
def display_books():
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
        # +2 to leave a little space before the next column and prevent them from being too close together.

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
            # +2 to leave a little space before the next column and prevent them from being too close together.

            if column_length < len(categories[book_details.index(detail)]):
                column_length = len(categories[book_details.index(detail)]) + 2

            print(f"{detail: <{column_length}}", end="")

        print("\n")


#Functional Requirement 2 - Search for Book
def search_books():
    """
    Prompts user to input ISBN, name of author and/or title.
    Displays header for the function.
    """
    print(
        r"""

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
░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░░╚═════╝░╚══════╝"""
    )

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

    print("\nBook Details Have Been Displayed.\n")
    print("Returning to Main Menu.")
    input("Press Any Key To Continue.")
    return 0


#Functional Requirement 3 - Add Book Record(s) 
def add_book(book_details):
    with open("books_23094907.txt", 'a') as f:
        isbn, author, title, publisher, genre, published_year, date_purchased_str, status = book_details
        book_information = f"{isbn}|{author}|{title}|{publisher}|{
            genre}|{published_year}|{date_purchased_str}|{status}"
        f.write('\n' + book_information)
    print("Book added successfully!")


#Functional Requirement 4 - Update Book Record(s)
def update_book(isbn, old_detail, new_detail, detail_type):
    """
    Opens book database in write mode and replaces old details with new details.
    We use ISBN to identify which item to update.
    """

    """
    We use a dictionary to determine which index to replace based on the detail type.
    """

    detail_to_index_identifier = {
        "isbn": 0,
        "author": 1,
        "title": 2,
        "publisher": 3,
        "genre": 4,
        "yop": 5,
        "dop": 6,
        "status": 7,
    }

    book_list = get_books()

    for book in book_list:
        """
        Finds the specific book to update.
        Updates the book details based on the detail type.
        Note that we use the detail_to_index_identifier dictionary to determine which index to replace.
        New details are updated in the book_list.
        """

        book_details = book.split("|")
        if book_details[0] == isbn:
            if book_details[detail_to_index_identifier[detail_type]] == old_detail:
                book_details[detail_to_index_identifier[detail_type]
                             ] = new_detail
                book_list[book_list.index(book)] = "|".join(book_details)

    """
    Opens book database in write mode and writes the updated book list, replacing the old book list.
    """

    with open("books_23094907.txt", "w") as f:
        f.write("\n".join(book_list))
    
    print("\nBook Updated Successfully!")
    input("Press Any Key To Continue.")
    return 0


#Functional Requirement 5 - Delete Book Record(s) 
def delete_book(isbn):
    book_list = get_books()

    # deletes book from book list
    for book in book_list:
        book = book.split("|")
        if isbn in book[0]:
            book_list.remove("|".join(book))
            break

    # writes the new updated book list into text file
    with open("books_23094907.txt", "w") as f:
        for book in book_list:
            f.write(book)
            f.write("\n")
        # removes the last newline character
        f.truncate(f.tell() - 1)

    print("Book Deleted Successfully!")
    print("\nReturning to Main Menu...")
    input("Press Any Key To Continue.")
    return 0


#Functional Requirement 6 - Exit Program
def exit_program(program_start_time):
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    time_spent = datetime.strptime(
        time_now, "%Y-%m-%d %H:%M:%S") - datetime.strptime(program_start_time, "%Y-%m-%d %H:%M:%S")

    # displays time in xx Hours xx Minutes xx Seconds format
    hours, minutes, seconds = str(time_spent).split(":")
    print(f"You Spent {hours} Hours {minutes} Minutes {
          seconds} Seconds using This Program.")
    user_option_exit = input("Are You Sure You Want To Exit? (Y/N): ").upper()

    '''
    Error Handling for User Input
    '''

    while (user_option_exit != "Y" and user_option_exit != "N"):
        print("Invalid Input. Please Input [Y]es / [N]o.")
        user_option_exit = input(
            "Are You Sure You Want To Exit? (Y/N): ").upper()

    if (user_option_exit == "Y"):
        print("\nExiting Program...")
        input("Press Any Key To Exit.")
        return True

    elif (user_option_exit == "N"):
        print("\nReturning To Main Menu...")
        input("Press Any Key To Continue.")
        return False


'''
Main Program Functional Requirements END
'''

'''
Function User Interface Functions START
'''


def display_book_interface():
    display_books()
    sort_books()

# user interface for add book function
def add_book_interface():
    clear()
    print(
        r"""
██████╗░░█████╗░░█████╗░██╗░░██╗  ░█████╗░██████╗░██████╗░██╗████████╗██╗░█████╗░███╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝  ██╔══██╗██╔══██╗██╔══██╗██║╚══██╔══╝██║██╔══██╗████╗░██║
██████╦╝██║░░██║██║░░██║█████═╝░  ███████║██║░░██║██║░░██║██║░░░██║░░░██║██║░░██║██╔██╗██║
██╔══██╗██║░░██║██║░░██║██╔═██╗░  ██╔══██║██║░░██║██║░░██║██║░░░██║░░░██║██║░░██║██║╚████║
██████╦╝╚█████╔╝╚█████╔╝██║░╚██╗  ██║░░██║██████╔╝██████╔╝██║░░░██║░░░██║╚█████╔╝██║░╚███║
╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝  ╚═╝░░╚═╝╚═════╝░╚═════╝░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝

██╗███╗░░██╗████████╗███████╗██████╗░███████╗░█████╗░░█████╗░███████╗
██║████╗░██║╚══██╔══╝██╔════╝██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝
██║██╔██╗██║░░░██║░░░█████╗░░██████╔╝█████╗░░███████║██║░░╚═╝█████╗░░
██║██║╚████║░░░██║░░░██╔══╝░░██╔══██╗██╔══╝░░██╔══██║██║░░██╗██╔══╝░░
██║██║░╚███║░░░██║░░░███████╗██║░░██║██║░░░░░██║░░██║╚█████╔╝███████╗
╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚══════╝
"""
    )

    print("\nWelcome to the Book Addition Interface!\n")

    '''
    - Display all books using display_books().
    - Prompts the user to input details for a new book by calling the add_book_information() function.
    - Attempts to add the new book to the collection using the add_book() function. If an error occurs during this process, it prints an error message and returns.
    - If the book is added successfully, it prints a success message and the details of the new book.
    - Ask the user if they want to add another book. If they do, it calls itself recursively to repeat the process. If not, it returns 0 to end the function.
    '''

    display_books()

    print("_____________________________________")
    print(f"\nAll books have been displayed.\n")
    print("To add a book, please input the book's details.\n")

    try:
        book = add_book_information()
        isbn, author, title, publisher, genre, yop, dop, status = book
    except Exception as e:
        print(f"An error occurred while adding the book: {str(e)}")

    '''
    Prints details of the book to add and double confirms with user whether they want to add the book.
    '''

    print("\n_____________________________________")
    print("\nPlease confirm the following details:\n")
    print(f"ISBN: {isbn}")
    print(f"Author: {author}")
    print(f"Title: {title}")
    print(f"Publisher: {publisher}")
    print(f"Genre: {genre}")
    print(f"Year of Publication: {yop}")
    print(f"Date of Purchase: {dop}")
    print(f"Status: {status}")

    print("\n_____________________________________")

    user_input_confirm = input(
        "\nAre you sure you want to add this book with the following details?\n[1] - Yes\n[2] - No\n\n")

    while user_input_confirm not in ["1", "2"]:
        print("\nAre you sure you want to add this book with the following details?\n")
        user_input_confirm = input(
            "\nAre you sure you want to add this book with the following details?\n[1] - Yes\n[2] - No\n\n")

    if (user_input_confirm == "1"):
        add_book(book)
    else:
        print("Okay. The Book will not be Added.")
        input("Press Any Key to Return to Main Menu.")
        return 0

    print(
        "\nCongratulations! Your Input is Valid and A Book Has Been Added!\n"
    )

    print(f"\nBook Added: {title} by {author}")
    print("\nBook Details:\n")
    print(f"ISBN: {isbn}")
    print(f"Author: {author}")
    print(f"Title: {title}")
    print(f"Publisher: {publisher}")
    print(f"Genre: {genre}")
    print(f"Year of Publication: {yop}")
    print(f"Date of Purchase: {dop}")
    print(f"Status: {status}")

    print("\nWould You Like to Add Another Book?\n")
    user_input_option = input("[1] - Yes\n[2] - No\n\n")

    while user_input_option not in ["1", "2"]:
        print("\nWould You Like to Add Another Book?\n")
        user_input_option = input(
            "[1] - Yes, Retry the Function\n[2] - No, Return to Main Menu.\n\n"
        )

    if user_input_option == "1":
        add_book_interface()

    elif user_input_option == "2":
        print("\nReturning to Main Menu...")
        input("Press Any Key to Continue.")
        return 0


# user interface for update book function
def update_book_interface():
    """
    Calls the clear function to clear the screen for better visiblity.
    Displays header for the function. (Book Update)
    """

    clear()
    print(
        r"""
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
╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚══════╝"""
    )

    print("\nWelcome to the Book Updating Interface!\n")

    """
    Displays all books in database.
    Allows user to clearly know what books are in the database and what details to update.
    """
    display_books()

    """
    Prompts user to input ISBN, author or title.
    """

    print("_____________________________________")
    print(f"\nAll Books Have Been Displayed.\n")
    print(
        "To Edit an Item, Please Input the Item's 13-digit ISBN, Author OR Book Title.\n"
    )

    book_isbn = input_to_isbn()
    book_details = isbn_to_details(book_isbn)

    if(book_isbn == 1):
        print("Retrying Function...")
        input("Input Any Key to Continue.")
        update_book_interface()
    
    elif(book_isbn == 0):
        print("Returning to Main Menu...")
        input("Input Any Key to Continue.")
        return 1
    

    """
    If user input is valid,
    Run through book list to find book with same ISBN, author or title.
    Displays details of books and prompts user input for what details to update.
    Also Clears screen for better visibility.
    """

    clear()
    print(
        r"""       
██████╗░░█████╗░░█████╗░██╗░░██╗  ███████╗░█████╗░██╗░░░██╗███╗░░██╗██████╗░██╗
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝  ██╔════╝██╔══██╗██║░░░██║████╗░██║██╔══██╗██║
██████╦╝██║░░██║██║░░██║█████═╝░  █████╗░░██║░░██║██║░░░██║██╔██╗██║██║░░██║██║
██╔══██╗██║░░██║██║░░██║██╔═██╗░  ██╔══╝░░██║░░██║██║░░░██║██║╚████║██║░░██║╚═╝
██████╦╝╚█████╔╝╚█████╔╝██║░╚██╗  ██║░░░░░╚█████╔╝╚██████╔╝██║░╚███║██████╔╝██╗
╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝  ╚═╝░░░░░░╚════╝░░╚═════╝░╚═╝░░╚══╝╚═════╝░╚═╝
"""
    )
    print(
        "\nCongratulations! Your Input is Valid and A Book Has Been Found!\n"
    )

    # gets all books in database
    book_list = get_books()

    # initialize isbn list to check for duplicates when updating books
    isbn_list = []

    for book in book_list:
        # temp variables assigned because we only use this for loop to search for the specific user-inputted book
        (
            temp_isbn,
            temp_author,
            temp_title,
            temp_publisher,
            temp_genre,
            temp_yop,
            temp_dop,
            temp_status,
        ) = book.split("|")

        # adds every book's isbn into isbn_list to check for duplicates
        isbn_list.append(temp_isbn)

        # displays book details

    isbn = book_details[0]
    author = book_details[1]
    title = book_details[2]
    publisher = book_details[3]
    genre = book_details[4]
    yop = book_details[5]
    dop = book_details[6]
    status = book_details[7]

    print(f"\nBook Found: {title} by {author}")
    print("\nBook Details:\n")
    print(f"ISBN: {isbn}")
    print(f"Author: {author}")
    print(f"Title: {title}")
    print(f"Publisher: {publisher}")
    print(f"Genre: {genre}")
    print(f"Year of Publication: {yop}")
    print(f"Date of Purchase: {dop}")
    print(f"Status: {status}")

    print("\n\nWhat Details Would You Like to Update?\n")


    # initialize variables to store old and new details
    old_detail = ""
    new_detail = ""
    detail_type = ""

    user_update_option = input(
        "[1] - ISBN\n[2] - Author\n[3] - Title\n[4] - Publisher\n[5] - Genre\n[6] - Year of Publication\n[7] - Date of Purchase\n[8] - Book Status\n\n"
    )

    if user_update_option not in [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
    ]:
        if user_error_redirect(
            "\nERROR: Invalid Input Detected. Please Input an Option between [1] - [4]."
        ):
            update_book_interface()
        else:
            return 0

    else:
        if user_update_option == "1":
            new_isbn = input("Please Input New ISBN (13 Digits):\n")

            if len(new_isbn) != 13:
                if user_error_redirect(
                    f"\nERROR: ISBN Should Contain EXACTLY 13 digits. Your Input Had {len(new_isbn)} digits."
                ):
                    update_book_interface()
                else:
                    return 0
            else:
                """
                If the user inputted new detail is the same as the old detail. Display message and informs user that no changes will be made.
                The same applies for the other details.
                """

                if new_isbn == isbn:
                    print(
                        f"\nThe New Inputted ISBN is the Same as the Old ISBN. No Changes Will Be Made."
                    )
                else:
                    """
                    If user inputs a new ISBN that already exists in the database,
                    returns an error message and redirects user to input error handling function.
                    """
                    if new_isbn in isbn_list:
                        if user_error_redirect(
                            f"\nERROR: ISBN {new_isbn} Already Exists in Database."
                        ):
                            update_book_interface()
                        else:
                            return 0

                    else:
                        old_detail = isbn
                        new_detail = new_isbn
                        detail_type = "isbn"

        elif user_update_option == "2":
            print(f"Current Author: {author}\n")
            new_author = input("Please Input New Author:\n")

            # '|' is not allowed because it will be used as a delimiter in the database
            while('|' in new_author):
                print("ERROR: Author cannot contain '|'. Please try again.\n")
                new_author = input("Please Input New Author:\n")
            
            if new_author == author:
                print(
                    f"\nThe New Inputted Author is the Same as the Old Author. No Changes Will Be Made."
                )

            else:
                old_detail = author
                new_detail = new_author
                detail_type = "author"

        elif user_update_option == "3":
            print(f"Current Title: {title}\n")
            new_title = input("Please Input New Title:\n")

            # '|' is not allowed because it will be used as a delimiter in the database
            while('|' in new_title):
                print("ERROR: Title cannot contain '|'. Please try again.\n")
                new_title = input("Please Input New Title:\n")

            if new_title == title:
                print(
                    f"\nThe New Inputted Title is the Same as the Old Title. No Changes Will Be Made."
                )

            else:
                old_detail = title
                new_detail = new_title
                detail_type = "title"

        elif user_update_option == "4":
            print(f"Current Publisher: {publisher}\n")
            new_publisher = input("Please Input New Publisher:\n")


            # '|' is not allowed because it will be used as a delimiter in the database
            while('|' in new_publisher):
                print("ERROR: Publisher cannot contain '|'. Please try again.\n")
                new_publisher = input("Please Input New Publisher:\n")

            if new_publisher == publisher:
                print(
                    f"\nThe New Inputted Publisher is the Same as the Old Publisher. No Changes Will Be Made."
                )

            else:
                old_detail = publisher
                new_detail = new_publisher
                detail_type = "publisher"

        elif user_update_option == "5":
            print(f"Current Genre: {genre}\n")
            new_genre = input("Please Input New Genre:\n")

            # '|' is not allowed because it will be used as a delimiter in the database
            while('|' in new_genre):
                print("ERROR: Genre cannot contain '|'. Please try again.\n")
                new_genre = input("Please Input New Genre:\n")

            if new_genre == genre:
                print(
                    f"\nThe New Inputted Genre is the Same as the Old Genre. No Changes Will Be Made."
                )

            else:
                old_detail = genre
                new_detail = new_genre
                detail_type = "genre"

        elif user_update_option == "6":
            print(f"Current Year of Publication: {yop}\n")
            new_yop = input("Please Input New Year of Publication:\n")

            if len(new_yop) != 4:
                if user_error_redirect(
                    f"\nERROR: Year of Publication Should Contain EXACTLY 4 digits. Your Input Had {len(new_yop)} digits."
                ):
                    update_book_interface()
                else:
                    return 0

            if new_yop == yop:
                print(
                    f"\nThe New Inputted Year of Publication is the Same as the Old Year of Publication. No Changes Will Be Made."
                )
            else:
                old_detail = yop
                new_detail = new_yop
                detail_type = "yop"

        elif user_update_option == "7":
            print(f"Current Date of Purchase: {dop}\n")
            new_dop = input(
                "Please Input New Date of Purchase (DD/MM/YYYY):\n"
            )

            if len(new_dop) != 10:
                if user_error_redirect(
                    f"\nERROR: Date of Purchase Should Contain EXACTLY 10 characters including '/'. Your Input Had {len(new_dop)} digits."
                ):
                    update_book_interface()
                else:
                    return 0

            dop_day, dop_month, dop_year = new_dop.split("/")

            if int(dop_day) > 31 or int(dop_day) < 1:
                if user_error_redirect(
                    f"\nERROR: Day of Purchase Should Be Between 1 and 31."
                ):
                    update_book_interface()
                else:
                    return 0

            if int(dop_month) > 12 or int(dop_month) < 1:
                if user_error_redirect(
                    f"\nERROR: Month of Purchase Should Be Between 1 and 12."
                ):
                    update_book_interface()
                else:
                    return 0

            if int(dop_year) > 2023 or int(dop_year) < 0:
                if user_error_redirect(
                    f"\nERROR: Year of Purchase Should Be Between 0 and 2023."
                ):
                    update_book_interface()
                else:
                    return 0

            if new_dop == dop:
                print(
                    f"\nThe New Inputted Date of Purchase is the Same as the Old Date of Purchase. No Changes Will Be Made."
                )
            else:
                old_detail = dop
                new_detail = new_dop
                detail_type = "dop"

        elif user_update_option == "8":
            print(f"Current Status: {status}\n")
            new_status = input(
                "Please Input New Status:\n[1] - Wishlist\n[2] - To-Read\n[3] - Reading\n[4] - Completed\n\n"
            )

            if new_status not in ["1", "2", "3", "4"]:
                if user_error_redirect(
                    "\nERROR: Invalid Input Detected. Please Input an Option between [1] - [4]."
                ):
                    update_book_interface()
                else:
                    return 0

            if new_status == "1":
                new_status = "wishlist"
            elif new_status == "2":
                new_status = "to-read"
            elif new_status == "3":
                new_status = "reading"
            else:
                new_status = "completed"

            if new_status == status:
                print(
                    f"\nThe New Inputted Status is the Same as the Old Status. No Changes Will Be Made."
                )

            else:
                old_detail = status
                new_detail = new_status
                detail_type = "status"

    
    if(detail_type == ""):
        print(
            "\nYour Inputted Details are The Same as The Previous Details. Thus, No Changes Will Be Made."
        )
        print(
            "\nNo Updates Will Be Made From Your Input.\nWould You Like to Try Again?\n"
        )
        user_input_option = input("[1] - Yes\n[2] - No\n\n")

        while user_input_option not in ["1", "2"]:
            # error handling: asks user for input again if input is invalid
            print(
                "\nNo Updates Will Be Made From Your Input.\nWould You Like to Try Again?\n"
            )
            user_input_option = input(
                "[1] - Yes, Retry the Function\n[2] - No, Return to Main Menu.\n\n"
            )

        if user_input_option == "1":
            update_book_interface()
        else:
            return 0
        
    else:
        #display book details again
        print("\n______________________________________________________________________________\n")
        print("Update Summary:\n")
        print(f"Old {detail_type.capitalize()}: {old_detail}")
        print(f"New {detail_type.capitalize()}: {new_detail}")

        # double confirms with user to confirm whether they want to update the selected book
        user_option = input(
            "\nAre you sure you want to update this book?\n[1] - Yes\n[2] - No\n"
        )

        # error handling
        if user_option not in ["1", "2"]:
            if user_error_redirect(
                "\nERROR: Invalid Input Detected. Please Input an Option between [1] - [2]."
            ):
                update_book_interface()
            else:
                return 0

        # updates book if user confirms, otherwise returns to main menu
        if user_option == "1":
            update_book(isbn, old_detail, new_detail, detail_type)
        elif user_option == "2":
            print("Okay. The Book will not be Updated.")
            input("Press Any Key to Return to Main Menu.")
            return 0


# user interface for delete book function
def delete_book_interface():
    clear()

    print(r'''
          
██████╗░███████╗██╗░░░░░███████╗████████╗███████╗  ██████╗░░█████╗░░█████╗░██╗░░██╗
██╔══██╗██╔════╝██║░░░░░██╔════╝╚══██╔══╝██╔════╝  ██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
██║░░██║█████╗░░██║░░░░░█████╗░░░░░██║░░░█████╗░░  ██████╦╝██║░░██║██║░░██║█████═╝░
██║░░██║██╔══╝░░██║░░░░░██╔══╝░░░░░██║░░░██╔══╝░░  ██╔══██╗██║░░██║██║░░██║██╔═██╗░
██████╔╝███████╗███████╗███████╗░░░██║░░░███████╗  ██████╦╝╚█████╔╝╚█████╔╝██║░╚██╗
╚═════╝░╚══════╝╚══════╝╚══════╝░░░╚═╝░░░╚══════╝  ╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝

██╗███╗░░██╗████████╗███████╗██████╗░███████╗░█████╗░░█████╗░███████╗
██║████╗░██║╚══██╔══╝██╔════╝██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝
██║██╔██╗██║░░░██║░░░█████╗░░██████╔╝█████╗░░███████║██║░░╚═╝█████╗░░
██║██║╚████║░░░██║░░░██╔══╝░░██╔══██╗██╔══╝░░██╔══██║██║░░██╗██╔══╝░░
██║██║░╚███║░░░██║░░░███████╗██║░░██║██║░░░░░██║░░██║╚█████╔╝███████╗
╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚══════╝''')

    print("\n______________________________________________________________________________\n")

    display_books()

    user_input = input_to_isbn()

    if (user_input == 1):
        delete_book_interface()
    elif (user_input == 0):
        return
    else:
        book_details = isbn_to_details(user_input)

        # display targeted book details
        print("\n______________________________________________________________________________\n")
        print("Book Details:")
        print("ISBN: " + book_details[0])
        print("Author: " + book_details[1])
        print("Title: " + book_details[2])
        print("Publisher: " + book_details[3])
        print("Genre: " + book_details[4])
        print("Year Published: " + book_details[5])
        print("Date Purchased: " + book_details[6])
        print("Status: " + book_details[7])
        print("\n______________________________________________________________________________\n")

        '''
        Double confirms with user to confirm whether they want to delete the selected book.
        '''
        user_option = input(
            "Are you sure you want to delete this book?\n[1] - Yes\n[2] - No\n")

        # error handling
        if (user_option not in ['1', '2']):
            print("Invalid Input!")
            user_option = input(
                "Are you sure you want to delete this book?\n[1] - Yes\n[2] - No\n")

        # deletes book if user confirms, otherwise returns to main menu
        if (user_option == "Y" or user_option == "1"):
            delete_book(user_input)
            return 0
        elif (user_option == "N" or user_option == "2"):
            print("Okay. The Book will not be Deleted.")
            input("Press Any Key to Return to Main Menu.")
            return 0
        

# function to display team background
def display_team_background():
    clear()

    print(
        r"""
████████╗███████╗░█████╗░███╗░░░███╗  ██████╗░░█████╗░░█████╗░██╗░░██╗░██████╗░██████╗░░█████╗░██╗░░░██╗███╗░░██╗██████╗░
╚══██╔══╝██╔════╝██╔══██╗████╗░████║  ██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝░██╔══██╗██╔══██╗██║░░░██║████╗░██║██╔══██╗
░░░██║░░░█████╗░░███████║██╔████╔██║  ██████╦╝███████║██║░░╚═╝█████═╝░██║░░██╗░██████╔╝██║░░██║██║░░░██║██╔██╗██║██║░░██║
░░░██║░░░██╔══╝░░██╔══██║██║╚██╔╝██║  ██╔══██╗██╔══██║██║░░██╗██╔═██╗░██║░░╚██╗██╔══██╗██║░░██║██║░░░██║██║╚████║██║░░██║
░░░██║░░░███████╗██║░░██║██║░╚═╝░██║  ██████╦╝██║░░██║╚█████╔╝██║░╚██╗╚██████╔╝██║░░██║╚█████╔╝╚██████╔╝██║░╚███║██████╔╝
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝  ╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝░╚════╝░░╚═════╝░╚═╝░░╚══╝╚═════╝░"""
    )

    print("\nTeam Member List\n")
    print("1) Darrance Beh Heng Shek (Team Lead)")
    print("2) Deron Ho Wen Harn")
    print("3) Izzat Zulqarnain Bin Izaiddin")
    print("4) Tan Ho Chen")
    print("5) Lee Ming Hui Isaac")

    print("\nProject Background\n")
    print(
        "- This project is a final group assessment for the subject CSC1024 - Programming Principles."
    )
    print(
        "- The project is a book management system that allows users to add, update, delete and view books in a database."
    )
    print(
        "- For this project, the team utilized the GitHub platform to collaborate on the project under the guidance of the Team Lead."
    )

    print(
        r"""
          
██████╗░██████╗░░█████╗░░░░░░██╗███████╗░█████╗░████████╗  ░█████╗░██████╗░███████╗██████╗░██╗████████╗░██████╗
██╔══██╗██╔══██╗██╔══██╗░░░░░██║██╔════╝██╔══██╗╚══██╔══╝  ██╔══██╗██╔══██╗██╔════╝██╔══██╗██║╚══██╔══╝██╔════╝
██████╔╝██████╔╝██║░░██║░░░░░██║█████╗░░██║░░╚═╝░░░██║░░░  ██║░░╚═╝██████╔╝█████╗░░██║░░██║██║░░░██║░░░╚█████╗░
██╔═══╝░██╔══██╗██║░░██║██╗░░██║██╔══╝░░██║░░██╗░░░██║░░░  ██║░░██╗██╔══██╗██╔══╝░░██║░░██║██║░░░██║░░░░╚═══██╗
██║░░░░░██║░░██║╚█████╔╝╚█████╔╝███████╗╚█████╔╝░░░██║░░░  ╚█████╔╝██║░░██║███████╗██████╔╝██║░░░██║░░░██████╔╝
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚══════╝░╚════╝░░░░╚═╝░░░  ░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝░░░╚═╝░░░╚═════╝░"""
    )
    print("\nDarrance Beh Heng Shek (Team Lead)")
    print("- Responsible for Managing the Team and the Project.")
    print(
        "- Ensures that the Project is on Track and that the Team is on Schedule to Meet Project Deadline."
    )
    print(
        "- Gave Guidance and Constructive Feedback to Team Members and Made Sure All Member's Work Meets Quality Standards."
    )
    print(
        "- Responsible for the Update Book Record(s) Functions, ALL Auxilary Functions, ALL Utility Functions, UI/UX Experience."
    )
    print(
        "- Responsible for Compiling Final Program and Bug-Testing The Program."
    )
    print("- Compiled the Final Report and Final Flowchart.")

    print("\nDeron Ho Wen Harn")
    print("- Responsible for the Display Book Record(s) Function.")
    print(
        "- Wrote Report Section and Drew Flowchart for their Responsible Function."
    )

    print("\nIzzat Zulqarnain Bin Izaiddin")
    print("- Responsible for the Search Book Record(s) Function.")
    print(
        "- Wrote Report Section and Drew Flowchart for their Responsible Function."
    )

    print("\nTan Ho Chen")
    print("- Partially Responsible for the Delete Book Record(s) Function.")
    print(
        "- Partially Responsible for Writing Report Section and Drawing Flowchart for their Responsible Function."
    )

    print("\nLee Ming Hui Isaac")
    print("- Responsible for the Add Book Record(s) Function.")
    print(
        "- Wrote Report Section and Drew Flowchart for their Responsible Function."
    )

    input("\n\nInput any Key to Return to Main Menu.\n")
    return 0


# main menu user interface
def main_user_interface():
    '''
    Calls the clear function to clear the screen for better visiblity.
    Displays header for the function. (Main Menu)
    '''

    clear()
    print(r"""
██████╗░███████╗██████╗░░██████╗░█████╗░███╗░░██╗░█████╗░██╗░░░░░  ██████╗░░█████╗░░█████╗░██╗░░██╗
██╔══██╗██╔════╝██╔══██╗██╔════╝██╔══██╗████╗░██║██╔══██╗██║░░░░░  ██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
██████╔╝█████╗░░██████╔╝╚█████╗░██║░░██║██╔██╗██║███████║██║░░░░░  ██████╦╝██║░░██║██║░░██║█████═╝░
██╔═══╝░██╔══╝░░██╔══██╗░╚═══██╗██║░░██║██║╚████║██╔══██║██║░░░░░  ██╔══██╗██║░░██║██║░░██║██╔═██╗░
██║░░░░░███████╗██║░░██║██████╔╝╚█████╔╝██║░╚███║██║░░██║███████╗  ██████╦╝╚█████╔╝╚█████╔╝██║░╚██╗
╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚══╝╚═╝░░╚═╝╚══════╝  ╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝

███╗░░░███╗░█████╗░███╗░░██╗░█████╗░░██████╗░███████╗███╗░░░███╗███████╗███╗░░██╗████████╗
████╗░████║██╔══██╗████╗░██║██╔══██╗██╔════╝░██╔════╝████╗░████║██╔════╝████╗░██║╚══██╔══╝
██╔████╔██║███████║██╔██╗██║███████║██║░░██╗░█████╗░░██╔████╔██║█████╗░░██╔██╗██║░░░██║░░░
██║╚██╔╝██║██╔══██║██║╚████║██╔══██║██║░░╚██╗██╔══╝░░██║╚██╔╝██║██╔══╝░░██║╚████║░░░██║░░░
██║░╚═╝░██║██║░░██║██║░╚███║██║░░██║╚██████╔╝███████╗██║░╚═╝░██║███████╗██║░╚███║░░░██║░░░
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░╚═════╝░╚══════╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░

░██████╗██╗░░░██╗░██████╗████████╗███████╗███╗░░░███╗   developed by:
██╔════╝╚██╗░██╔╝██╔════╝╚══██╔══╝██╔════╝████╗░████║   1) Darrance Beh Heng Shek (Team Lead)
╚█████╗░░╚████╔╝░╚█████╗░░░░██║░░░█████╗░░██╔████╔██║   2) Deron Ho Wen Harn
░╚═══██╗░░╚██╔╝░░░╚═══██╗░░░██║░░░██╔══╝░░██║╚██╔╝██║   3) Izzat Zulqarnain Bin Izaiddin
██████╔╝░░░██║░░░██████╔╝░░░██║░░░███████╗██║░╚═╝░██║   4) Tan Ho Chen
╚═════╝░░░░╚═╝░░░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░░░░╚═╝   5) Lee Ming Hui Isaac""")

    print("\nWelcome to your Personal Book Management System!\n")
    # displays current time in YYYY-MM-DD HH:MM:SS format
    print(f"The Current Time is {
          datetime.now().strftime("%Y-%m-%d %H:%M:%S")}")

    print(r"""
███████╗██╗░░░██╗███╗░░██╗░█████╗░████████╗██╗░█████╗░███╗░░██╗  ██╗░░░░░██╗░██████╗████████╗
██╔════╝██║░░░██║████╗░██║██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║  ██║░░░░░██║██╔════╝╚══██╔══╝
█████╗░░██║░░░██║██╔██╗██║██║░░╚═╝░░░██║░░░██║██║░░██║██╔██╗██║  ██║░░░░░██║╚█████╗░░░░██║░░░
██╔══╝░░██║░░░██║██║╚████║██║░░██╗░░░██║░░░██║██║░░██║██║╚████║  ██║░░░░░██║░╚═══██╗░░░██║░░░
██║░░░░░╚██████╔╝██║░╚███║╚█████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║  ███████╗██║██████╔╝░░░██║░░░
╚═╝░░░░░░╚═════╝░╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝  ╚══════╝╚═╝╚═════╝░░░░╚═╝░░░""")

    print("\nWhat Would You Like to Do?\n")

    print("[1] - Display All Book Records in Database\n[2] - Search for a Book in Database\n[3] - Add Book Record(s) into Database\n[4] - Update Book Record(s) in Database\n[5] - Delete Book Record(s) from Database\n[6] - Show Team Background\n\n[x] - Exit the Program\n\n")

    user_input_function_option = input("Input Option Here: ")

    '''
    Error handling for user input if input is not in the options.
    '''

    while (user_input_function_option not in ['1', '2', '3', '4', '5', 'x']):
        print("\nInvalid Input Detected. Please Try Again.")
        user_input_function_option = input(
            "Input Option Here: ")

    option_to_function_identifier = {
        "1": display_book_interface,
        "2": search_books,
        "3": add_book_interface,
        "4": update_book_interface,
        "5": delete_book_interface,
        "6": display_team_background
    }

    if (user_input_function_option == 'x'):
        return 0
    else:
        option_to_function_identifier[user_input_function_option]()





'''
Function User Interface Functions END
'''


'''
Master Function VVV
Runs at program start
'''


def main():
    initial_time_program_start = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    while True:
        if(main_user_interface() == 0):
            break
    '''
    If function returns false, it means the user changed their mind and doesn't want to exit.
    Thus, function redirects user back to main menu.
    The function will exit the program if user decides to exit and will not redirect back to this function.
    '''

    # calls exit_program with initial time of program start as parameter to calculate total time used in program
    if (not exit_program(initial_time_program_start)):
        main_user_interface()
    else:
        return None


if __name__ == "__main__":
    main()

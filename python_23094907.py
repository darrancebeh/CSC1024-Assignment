import os
# import os for terminal screen clearing

''' 
Utility Functions START
'''


def clear():
    '''
    Function to clear terminal screen.
    '''

    os.system('cls' if os.name == 'nt' else 'clear')


def user_error_redirect(message):
    '''
    Clears screen for visibility and displays error header.
    '''
    clear()
    print(r"""
███████╗██████╗░██████╗░░█████╗░██████╗░  ░█████╗░░█████╗░░█████╗░██╗░░░██╗██████╗░███████╗██████╗░██╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔══██╗██╔══██╗██╔══██╗██║░░░██║██╔══██╗██╔════╝██╔══██╗██║
█████╗░░██████╔╝██████╔╝██║░░██║██████╔╝  ██║░░██║██║░░╚═╝██║░░╚═╝██║░░░██║██████╔╝█████╗░░██║░░██║██║
██╔══╝░░██╔══██╗██╔══██╗██║░░██║██╔══██╗  ██║░░██║██║░░██╗██║░░██╗██║░░░██║██╔══██╗██╔══╝░░██║░░██║╚═╝
███████╗██║░░██║██║░░██║╚█████╔╝██║░░██║  ╚█████╔╝╚█████╔╝╚█████╔╝╚██████╔╝██║░░██║███████╗██████╔╝██╗
╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝  ░╚════╝░░╚════╝░░╚════╝░░╚═════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝""")

    print("\nOh No! Looks Like You Inputted Something Wrong!\n")
    print(f"Error Encountered: {message}\n")
    print("Please Read Prompt Instructions Carefully and Try Again!\n")

    '''
    Function to let user decide whether to retry input upon error or redirect to main menu.
    '''

    user_input_option = input(
        "\nRetry Input?\n[1] - Retry Input.\n[2] - Back to Main Menu.\n")

    '''
    Ensures that user input is either 1 or 2.
    '''

    while (user_input_option != '1' and user_input_option != '2'):
        print("\nInvalid Input Detected. Please Try Again.")
        user_input_option = input(
            "Retry Input?\n[1] - Retry Input.\n[2] - Back to Main Menu.\n")

    '''
    Returns True if user decides to retry input.
    Returns False if user decides to return to main menu.
    '''

    if (user_input_option == '1'):
        return True
    else:
        return False


'''
Utility Functions END
'''


'''
Auxilarty Functions START
'''

# function to get all books and details in database


def get_books():
    """
    Returns a list of all books in the database.
    """

    with open("books_23094907.txt", "r") as f:
        '''
        Returns all lines contained in the text file and separates every list item by line.
        '''
        book_list = f.read().split("\n")
        return book_list


# function to check if an author has multiple books in database
def check_author_multiple_book(author):
    '''
    Given author name, checks if author has multiple books in database.
    If author has multiple books, return list of all books of author.
    Else, return False.
    '''
    book_list = get_books()
    author_book_list = []
    for book in book_list:
        book_details = book.split("|")
        if (book_details[1] == author):
            author_book_list.append(book_details)

    if (len(author_book_list) > 1):
        return author_book_list
    else:
        return False


'''
Auxilarty Functions END
'''


'''
Main Program CRUD Functions START
'''

# update book function


def update_book(old_detail, new_detail, detail_type):
    '''
    Opens book database in write mode and replaces old details with new details.
    We use ISBN to identify which item to update.
    '''

    '''
    We use a dictionary to determine which index to replace based on the detail type.
    '''

    detail_to_index_identifier = {
        "isbn": 0,
        "author": 1,
        "title": 2,
        "publisher": 3,
        "genre": 4,
        "yop": 5,
        "dop": 6,
        "status": 7
    }

    book_list = get_books()

    for book in book_list:

        '''
        Finds the specific book to update.
        Updates the book details based on the detail type.
        Note that we use the detail_to_index_identifier dictionary to determine which index to replace.
        New details are updated in the book_list.
        '''

        book_details = book.split("|")
        if (book_details[detail_to_index_identifier[detail_type]] == old_detail):
            book_details[detail_to_index_identifier[detail_type]] = new_detail
            book_list[book_list.index(book)] = "|".join(book_details)

    '''
    Opens book database in write mode and writes the updated book list, replacing the old book list.
    '''

    with open("books_23094907.txt", "w") as f:
        f.write("\n".join(book_list))


'''
Main Program CRUD Functions END
'''

'''
Main Program User Interfaces START
'''


def update_book_interface():
    '''
    Calls the clear function to clear the screen for better visiblity.
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

    '''
    Displays all books in database.
    Allows user to clearly know what books are in the database and what details to update.
    '''

    print("Displaying All Books in Database...")
    print("Book details have been shortened for readability. In order to view full details, please navigate to display book feature in main menu.")
    print(
        "\nFormat: [Count] | ISBN | Author | Title | Genre | Current Status\n")

    book_count = 0
    book_list = get_books()

    '''
    ISBN, author and title list initialized for user input validation.
    '''

    isbn_list = []
    author_list = []
    title_list = []

    '''
    Books in book list are split into individual details.
    '''

    for book in book_list:
        book_count += 1
        isbn, author, title, publisher, genre, yop, dop, status = book.split(
            "|")
        print(f"[{book_count}] | {isbn} | {
              author} | {title} | {genre} | {status}")

        isbn_list.append(isbn)
        author_list.append(author)
        title_list.append(title)
    print(f"\nTotal Book Count: {book_count}\n")

    '''
    Prompts user to input ISBN, author or title.
    '''

    print(f"\nAll Books Have Been Displayed.\n")
    print("To Edit an Item, Please Input the Item's 13-digit ISBN, Author OR Book Title.\n")

    user_input_id = input("ISBN / Author / Title:\n")

    '''
    Checks if user inputted digits or text.
    '''

    if (user_input_id.isdigit()):
        '''
        If user attempted to input ISBN but length is not equal to 13, 
        returns an error message as ISBN contains exactly 13 characters.
        '''

        if (len(user_input_id) != 13):

            '''
            Redirects user to retry input or return to main menu.
            '''

            if (user_error_redirect(f"\nERROR: ISBN Should Contain EXACTLY 13 digits. Your Input Had {
                    len(user_input_id)} digits.")):
                update_book_interface()
            else:
                return 0

        else:

            '''
            If user inputted ISBN that is not in ISBN list,
            returns an error message and redirects user to input error handling function.
            '''

            if (user_input_id not in isbn_list):
                if (user_error_redirect(f"\nERROR: ISBN {user_input_id} Not Found in Database.")):
                    update_book_interface()
                else:
                    return 0

    else:
        '''
        If user inputted text, 
        Convert text and author and title list to lower-case for better data validation.
        Checks if text input is in author or title list.
        '''

        author_list_lower = [author.lower() for author in author_list]
        title_list_lower = [title.lower() for title in title_list]

        if (user_input_id.lower() not in author_list_lower and user_input_id.lower() not in title_list_lower):
            if (user_error_redirect(f"\nERROR: {user_input_id} Not Found in Database. Please Enter a Valid ISBN, Author or Title.")):
                update_book_interface()
            else:
                return 0

        else:
            '''
            If user input in lower case is in author list or title list,
            convert user input to correct case.
            This is to allow for easier data validation later on.
            '''

            if (user_input_id.lower() in author_list_lower):
                user_input_id = author_list[author_list_lower.index(
                    user_input_id.lower())]
            else:
                user_input_id = title_list[title_list_lower.index(
                    user_input_id.lower())]

            ''''
            If user inputted author name,
            Run check_author_multiple_book function to check if author has multiple books in database.
            '''

            if (user_input_id in author_list):
                author_book_list = check_author_multiple_book(user_input_id)

                '''
                Function returns a list of books with same author if author has multiple books.
                Else, function returns False.
                '''

                if (author_book_list):
                    print(f"\nMultiple Books Found for Author {
                          user_input_id}.")
                    print("Please Select the Book to Update:\n")
                    book_count = 0

                    '''
                    Displays all books under the author's name
                    '''

                    for book in author_book_list:
                        book_count += 1
                        isbn, author, title, publisher, genre, yop, dop, status = book

                        print(f"[{book_count}] | {isbn} | {
                              title} | {genre} | {status}")

                    '''
                    Prompts user to input book number to update.
                    '''

                    user_input_book_number = input(
                        f"\nPlease Input Book Number to Update: [1] - [{book_count}]\n")

                    if (user_input_book_number not in [str(i) for i in range(1, book_count + 1)]):
                        '''
                        Data validation to ensure that user input is a valid book number.
                        '''

                        if (user_error_redirect(f"\nERROR: Invalid Input Detected. Please Input an Option between [1] - [{book_count}].")):
                            update_book_interface()
                        else:
                            return 0
                    else:
                        '''
                        If user input is valid,
                        Assigns user inputted book number to associated book ISBN.
                        Filtering books by ISBN makes more sense and is more optimal for data validation.
                        This is because ISBN is unique to each book and WILL NOT HAVE duplicates.
                        '''

                        user_input_id = author_book_list[int(
                            user_input_book_number) - 1][0]

                else:
                    '''
                    If no duplicate author-book is found, (meaning that author only has 1 book in database)
                    auto-assign user inputted author name to associated book ISBN.
                    Filtering books by ISBN makes more sense and is more optimal for data validation.
                    This is because ISBN is unique to each book and WILL NOT HAVE duplicates.
                    '''

                    '''
                    Converts user input to correct author name case.
                    '''
                    if (user_input_id.lower() in author_list_lower):
                        user_input_id = author_list[author_list_lower.index(
                            user_input_id.lower())]

                    '''
                    Runs through the book list to find book with same author name.
                    Assigns book ISBN to user input.
                    '''
                    for book in book_list:
                        isbn, author, title, publisher, genre, yop, dop, status = book.split(
                            "|")
                        if (author == user_input_id):
                            user_input_id = isbn

    '''
    If user input is valid,
    Run through book list to find book with same ISBN, author or title.
    Displays details of books and prompts user input for what details to update.
    Also Clears screen for better visibility.
    '''

    clear()
    print(r"""       
██████╗░░█████╗░░█████╗░██╗░░██╗  ███████╗░█████╗░██╗░░░██╗███╗░░██╗██████╗░██╗
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝  ██╔════╝██╔══██╗██║░░░██║████╗░██║██╔══██╗██║
██████╦╝██║░░██║██║░░██║█████═╝░  █████╗░░██║░░██║██║░░░██║██╔██╗██║██║░░██║██║
██╔══██╗██║░░██║██║░░██║██╔═██╗░  ██╔══╝░░██║░░██║██║░░░██║██║╚████║██║░░██║╚═╝
██████╦╝╚█████╔╝╚█████╔╝██║░╚██╗  ██║░░░░░╚█████╔╝╚██████╔╝██║░╚███║██████╔╝██╗
╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝  ╚═╝░░░░░░╚════╝░░╚═════╝░╚═╝░░╚══╝╚═════╝░╚═╝
""")
    print("\nCongratulations! Your Input is Valid and A Book Has Been Found!\n")
    for book in book_list:
        isbn, author, title, publisher, genre, yop, dop, status = book.split(
            "|")
        if (isbn == user_input_id or author == user_input_id or title == user_input_id):
            print(f"\nBook Found: {title} by {author}")
            print("Book Details:\n")
            print(f"ISBN: {isbn}")
            print(f"Author: {author}")
            print(f"Title: {title}")
            print(f"Publisher: {publisher}")
            print(f"Genre: {genre}")
            print(f"Year of Publication: {yop}")
            print(f"Date of Purchase: {dop}")
            print(f"Status: {status}")

            print("What Details Would You Like to Update?\n")
            user_update_option = input(
                "[1] - ISBN\n[2] - Author\n[3] - Title\n[4] - Publisher\n[5] - Genre\n[6] - Year of Publication\n[7] - Date of Purchase\n[8] - Book Status\n\n")

            if (user_update_option not in ['1', '2', '3', '4', '5', '6', '7', '8']):
                if (user_error_redirect("\nERROR: Invalid Input Detected. Please Input an Option between [1] - [4].")):
                    update_book_interface()
                else:
                    return 0

            else:
                if (user_update_option == '1'):
                    new_isbn = input(
                        "Please Input New ISBN (13 Digits):\n")

                    if (len(new_isbn) != 13):
                        if (user_error_redirect(f"\nERROR: ISBN Should Contain EXACTLY 13 digits. Your Input Had {len(new_isbn)} digits.")):
                            update_book_interface()
                        else:
                            return 0
                    else:
                        if (new_isbn in isbn_list):
                            if (user_error_redirect(f"\nERROR: ISBN {new_isbn} Already Exists in Database.")):
                                update_book_interface()
                            else:
                                return 0

                        else:
                            update_book(
                                isbn, new_isbn, "isbn")

                elif (user_update_option == '2'):
                    print(
                        f"Current Author: {author}\n")
                    new_author = input(
                        "Please Input New Author:\n")
                    update_book(
                        author, new_author, "author")

                elif (user_update_option == '3'):
                    print(
                        f"Current Title: {title}\n")
                    new_title = input(
                        "Please Input New Title:\n")
                    update_book(
                        title, new_title, "title")

                elif (user_update_option == '4'):
                    print(
                        f"Current Publisher: {publisher}\n")
                    new_publisher = input(
                        "Please Input New Publisher:\n")
                    update_book(
                        publisher, new_publisher, "publisher")

                elif (user_update_option == '5'):
                    print(
                        f"Current Genre: {genre}\n")
                    new_genre = input(
                        "Please Input New Genre:\n")
                    update_book(
                        genre, new_genre, "genre")

                elif (user_update_option == '6'):
                    print(
                        f"Current Year of Publication: {yop}\n")
                    new_yop = input(
                        "Please Input New Year of Publication:\n")
                    if (len(new_yop) != 4):
                        if (user_error_redirect(f"\nERROR: Year of Publication Should Contain EXACTLY 4 digits. Your Input Had {len(new_yop)} digits.")):
                            update_book_interface()
                        else:
                            return 0
                    update_book(
                        yop, new_yop, "yop")

                elif (user_update_option == '7'):
                    print(
                        f"Current Date of Purchase: {dop}\n")
                    new_dop = input(
                        "Please Input New Date of Purchase:\n")
                    update_book(
                        dop, new_dop, "dop")

                elif (user_update_option == '8'):
                    print(
                        f"Current Status: {status}\n")
                    new_status = input(
                        "Please Input New Status:\n[1] - Wishlist\n[2] - To-Read\n[3] - Reading\n[4] - Completed\n\n")

                    if (new_status not in ["1", "2", "3", "4"]):
                        if (user_error_redirect("\nERROR: Invalid Input Detected. Please Input an Option between [1] - [4].")):
                            update_book_interface()
                        else:
                            return 0

                    if (new_status == '1'):
                        new_status = "wishlist"
                    elif (new_status == '2'):
                        new_status = "to-read"
                    elif (new_status == '3'):
                        new_status = "reading"
                    else:
                        new_status = "completed"

                    update_book(
                        status, new_status, "status")


'''
Main Program User Interfaces END
'''

from aux1_get_books import get_books
from aux3_user_error_option import user_error_redirect
from aux2_check_author_multiple_book import check_author_multiple_book


def input_to_isbn():
    '''
    Gets all books in database.
    '''
    book_list = get_books()
    '''
    ISBN, author and title list initialized for user input validation.
    '''

    isbn_list = []
    author_list = []
    title_list = []

    for book in book_list:
        isbn, author, title, publisher, genre, yop, dop, status = book.split(
            "|")

        isbn_list.append(isbn)
        author_list.append(author)
        title_list.append(title)

    user_input_id = input("Please Input Book ISBN / Author / Title:\n")

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
                return 1
            else:
                return 0

        else:

            '''
            If user inputted ISBN that is not in ISBN list,
            returns an error message and redirects user to input error handling function.
            '''

            if (user_input_id not in isbn_list):
                if (user_error_redirect(f"\nERROR: ISBN {user_input_id} Not Found in Database.")):
                    return 1
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
                return 1
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
                            return 1
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

            else:
                '''
                If user inputted title,
                Run through book list to find book with same title.
                Assigns book ISBN to user input.
                '''

                for book in book_list:
                    isbn, author, title, publisher, genre, yop, dop, status = book.split(
                        "|")
                    if (title == user_input_id):
                        user_input_id = isbn

    return user_input_id

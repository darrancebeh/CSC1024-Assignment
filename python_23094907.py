import os
import datetime
# import os for terminal screen clearing
# import datetime for date and time functions for user experience improvement

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
███████╗██████╗░██████╗░░█████╗░██████╗░  ░█████╗░░█████╗░░█████╗░██╗░░░██╗██████╗░██████╗░███████╗██████╗░██╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔══██╗██╔══██╗██╔══██╗██║░░░██║██╔══██╗██╔══██╗██╔════╝██╔══██╗██║
█████╗░░██████╔╝██████╔╝██║░░██║██████╔╝  ██║░░██║██║░░╚═╝██║░░╚═╝██║░░░██║██████╔╝██████╔╝█████╗░░██║░░██║██║
██╔══╝░░██╔══██╗██╔══██╗██║░░██║██╔══██╗  ██║░░██║██║░░██╗██║░░██╗██║░░░██║██╔══██╗██╔══██╗██╔══╝░░██║░░██║╚═╝
███████╗██║░░██║██║░░██║╚█████╔╝██║░░██║  ╚█████╔╝╚█████╔╝╚█████╔╝╚██████╔╝██║░░██║██║░░██║███████╗██████╔╝██╗
╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝  ░╚════╝░░╚════╝░░╚════╝░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝""")

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
Auxilary Functions START
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
Auxilary Functions END
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


def team_background():
    pass


def exit_program(program_start_time):
    time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    time_spent = datetime.datetime.strptime(
        time_now, "%Y-%m-%d %H:%M:%S") - datetime.datetime.strptime(program_start_time, "%Y-%m-%d %H:%M:%S")

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
        exit()

    elif (user_option_exit == "N"):
        print("\nReturning To Main Menu...")
        input("Press Any Key To Continue.")
        return False


def add_book_interface():
    pass


def delete_book_interface():
    pass


def display_book_interface():
    pass


def search_book_interface():
    pass


def update_book_interface():
    pass


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
          datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}")

    print(r"""
███████╗██╗░░░██╗███╗░░██╗░█████╗░████████╗██╗░█████╗░███╗░░██╗  ██╗░░░░░██╗░██████╗████████╗
██╔════╝██║░░░██║████╗░██║██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║  ██║░░░░░██║██╔════╝╚══██╔══╝
█████╗░░██║░░░██║██╔██╗██║██║░░╚═╝░░░██║░░░██║██║░░██║██╔██╗██║  ██║░░░░░██║╚█████╗░░░░██║░░░
██╔══╝░░██║░░░██║██║╚████║██║░░██╗░░░██║░░░██║██║░░██║██║╚████║  ██║░░░░░██║░╚═══██╗░░░██║░░░
██║░░░░░╚██████╔╝██║░╚███║╚█████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║  ███████╗██║██████╔╝░░░██║░░░
╚═╝░░░░░░╚═════╝░╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝  ╚══════╝╚═╝╚═════╝░░░░╚═╝░░░""")

    print("\nWhat Would You Like to Do?\n")

    print("[1] - View All Books in Database\n[2] - Search for a Book a Database\n[3] - Add a Book to Database\n[4] - Update a Book in Database\n[5] - Delete a Book in Database\n[6] - Display Team Background\n[x] - Exit Program\n\n")

    user_input_function_option = input("Input Option Here: ")

    '''
    Error handling for user input if input is not in the options.
    '''

    while (user_input_function_option not in ['1', '2', '3', '4', '5', '6', 'x']):
        print("\nInvalid Input Detected. Please Try Again.")
        user_input_function_option = input(
            "Input Option Here: ")

    option_to_function_identifier = {
        "1": display_books,
        "2": search_book,
        "3": add_book_interface,
        "4": update_book_interface,
        "5": delete_book_interface,
        "6": team_background
    }

    if (user_input_function_option == 'x'):
        return 0
    else:
        option_to_function_identifier[user_input_function_option]()


'''
Main Program User Interfaces END
'''


'''
Master Function VVV
'''


def main():
    initial_time_program_start = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    main_user_interface()

    '''
    If function returns false, it means the user changed their mind and doesn't want to exit.
    Thus, function redirects user back to main menu.
    The function will exit the program if user decides to exit and will not redirect back to this function.
    '''

    # calls exit_program with initial time of program start as parameter to calculate total time used in program
    if (not exit_program(initial_time_program_start)):
        main()
    else:
        return None


if __name__ == "__main__":
    main()

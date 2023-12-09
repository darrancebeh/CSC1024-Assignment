import os
import datetime
# import os for terminal screen clearing
# import datetime for date and time functions for user experience improvement

''' 
Utility Functions START
'''


'''
Utility Functions END
'''


'''
Auxilary Functions START
'''

# function to get all books and details in database


def get_books():
    pass


# function to check if an author has multiple books in database
def check_author_multiple_book(author):
    pass


'''
Auxilary Functions END
'''


'''
Main Program CRUD Functions START
'''

# update book function


def update_book(old_detail, new_detail, detail_type):
    pass


'''
Main Program CRUD Functions END
'''

'''
Main Program User Interfaces START
'''


def team_background():
    pass


def exit_program(program_start_time):
    pass


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
    pass


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

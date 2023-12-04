import os


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

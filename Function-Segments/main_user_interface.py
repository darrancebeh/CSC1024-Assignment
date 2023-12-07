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

███╗░░░███╗░█████╗░███╗░░██╗░█████╗░░██████╗░░█████╗░███╗░░░███╗███████╗███╗░░██╗████████╗
████╗░████║██╔══██╗████╗░██║██╔══██╗██╔════╝░██╔══██╗████╗░████║██╔════╝████╗░██║╚══██╔══╝
██╔████╔██║███████║██╔██╗██║███████║██║░░██╗░███████║██╔████╔██║█████╗░░██╔██╗██║░░░██║░░░
██║╚██╔╝██║██╔══██║██║╚████║██╔══██║██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░██║╚████║░░░██║░░░
██║░╚═╝░██║██║░░██║██║░╚███║██║░░██║╚██████╔╝██║░░██║██║░╚═╝░██║███████╗██║░╚███║░░░██║░░░
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░

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

    print("[1] - View All Books in Database\n[2] - Add a Book to Database\n[3] - Update a Book in Database\n[4] - Delete a Book from Database\n[5] - Background of Our Project\n\n[x] - Exit the Program\n\n")

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
        "2": add_book_interface,
        "3": update_book_interface,
        "4": delete_book_interface,
        "5": team_background
    }

    if (user_input_function_option == 'x'):
        return 0
    else:
        option_to_function_identifier[user_input_function_option]()


main_user_interface()

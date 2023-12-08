import datetime


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
        return True

    elif (user_option_exit == "N"):
        print("\nReturning To Main Menu...")
        input("Press Any Key To Continue.")
        return False

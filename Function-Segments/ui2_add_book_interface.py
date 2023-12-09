import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_books():
    pass


def add_book_interface():
    from add_book import add_book, add_book_information
    clear()
    print(r"""
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
""")

    print("\nWelcome to the book addition interface!\n")
    try:
        display_books()
    except Exception as e:
        print(f"An error occurred while displaying the books: {str(e)}")
        return

    print("_____________________________________")
    print(f"\nAll books have been displayed.\n")
    print("To add a book, please input the book's details.\n")

    try:
        book = add_book_information()
        isbn, author, title, publisher, genre, yop, dop, status = book
        add_book(book)
    except Exception as e:
        print(f"An error occurred while adding the book: {str(e)}")
        return

    print("\nCongratulations! Your Input is Valid and A Book Has Been Added!\n")

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

    while (user_input_option not in ["1", "2"]):
        print("\nWould You Like to Add Another Book?\n")
        user_input_option = input(
            "[1] - Yes, Retry the Function\n[2] - No, Return to Main Menu.\n\n")

    if (user_input_option == "1"):
        add_book_interface()
    else:
        return 0


add_book_interface()

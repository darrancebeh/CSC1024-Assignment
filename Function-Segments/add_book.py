'''
- The statement `from datetime import datetime` is used to directly import the `datetime` class from the `datetime` module.
- Commonly used for handling dates and times.
'''
from datetime import datetime

'''
- The 'def check_isbn_duplicate(isbn)' is responsible for checking existing ISBNs. 
- It checks books_23094907.txt in read mode for similarities. 
'''


def check_isbn_duplicate(isbn):
    with open("books_23094907.txt", 'r') as f:
        for line in f:
            if line.split('|')[0] == isbn:
                return True
    return False


'''
- The 'add_book_information()' function collects and validates information about a book from the user.
- It prompts the user to enter the ISBN, author's name, book's title, publisher's name, genre, publishing year, purchase date, and book's status.
- The naming convention is taken into consideration as people from different cultures have different naming conventions, such as umlauts and ligatures.
- Also performs validation checks for the ISBN to detect existing matching books.
'''


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
                "Error. ISBN number must be 13 digits long and contain only digits. Please try again.")
    while True:
        author = input("Author's name: ")
        if all(word.isalpha() for word in author.split()):
            break
        else:
            print(
                "Error. Author's name must only contain alphabetical characters. Please try again.")
    title = input("Book's title: ")
    publisher = input("Publisher's name: ")
    while True:
        genre = input("Genre of the book: ")
        if all(word.isalpha() for word in genre.split()):
            break
        else:
            print(
                "Error. Genre must only contain alphabetical characters. Please try again.")
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
                    "Error. The purchase date cannot be in the future and must be after the publishing year. Please try again.")
        except ValueError:
            print("Error. The date format is incorrect. Please try again.")
    while True:
        print("Please input the book's status:")
        print("[1] - Wishlist")
        print("[2] - To-read")
        print("[3] - Reading")
        print("[4] - Completed")
        print()
        status_input = input("Book's status (enter a number from 1 to 4): ")
        status_options = {'1': 'Wishlist', '2': 'To-read',
                          '3': 'Reading', '4': 'Completed'}
        if status_input in status_options:
            status = status_options[status_input]
            break
        else:
            print("Error. Invalid status. Please try again.")

    return isbn, author, title, publisher, genre, published_year, date_purchased_str, status


'''
- The 'def add_book(book)' function inserts the accepted details into books_23094907.txt in a specific format.
- Print out "Book added successfully!" if it's successful.
'''


def add_book(book):
    with open("books_23094907.txt", 'a') as f:
        isbn, author, title, publisher, genre, published_year, date_purchased_str, status = book
        book_information = f"{isbn}|{author}|{title}|{publisher}|{
            genre}|{published_year}|{date_purchased_str}|{status}"
        f.write('\n' + book_information)
    print("Book added successfully!")


'''
- Calls the 'add_book_information()' function to collect book information from the user.
- Collected information is then passed to the 'add_book()' function to add the book to the 'books_23094907.txt' file.
'''
book = add_book_information()
add_book(book)

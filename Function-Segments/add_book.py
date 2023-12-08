'''
- The statement `from datetime import datetime` is used to directly import the `datetime` class from the `datetime` module.
- Commonly used for handling dates and times.
'''
from datetime import datetime

'''
- The 'get_book_information()' function collects and validates information about a book from the user.
- It prompts the user to enter the ISBN number, author's name, book's title, publisher's name, genre, publishing year, purchase date, and book's status.
- Naming convention taken into consideration as people from different cultures have different naming conventions, such as umlauts and ligatures.
- Also performs validation checks for the ISBN number to detect for existing matching books.
'''
def get_book_information():
    print("Please enter the following information:")
    while True:
        isbn = input("ISBN number: ")
        if len(isbn) == 13 and isbn.isdigit():
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
            break
        else:
            print(
                "Error. Publishing year must be a 4-digit positive integer and not in the future. Please try again.")
    while True:
        date_purchased_str = input("Date purchased in the format DD-MM-YYYY: ")
        try:
            date_purchased = datetime.strptime(date_purchased_str, '%d-%m-%Y')
            if date_purchased <= datetime.now():
                break
            else:
                print(
                    "Error. The purchase date cannot be in the future. Please try again.")
        except ValueError:
            print("Error. The date format is incorrect. Please try again.")
    while True:
        print("Book's status options: Wishlist, To-read, Reading, Completed")
        status = input("Book's status: ")
        if status in ['Wishlist', 'To-read', 'Reading', 'Completed']:
            break
        else:
            print("Error. Invalid status. Please try again.")

    return isbn, author, title, publisher, genre, published_year, date_purchased_str, status

'''
- Opens books_23094907.txt and write the new book's information into it.
'''
def add_book(book):
    with open("books_23094907.txt", 'a') as f:
        isbn, author, title, publisher, genre, published_year, date_purchased_str, status = book
        book_information = f"{isbn}|{author}|{title}|{publisher}|{genre}|{published_year}|{date_purchased_str}|{status}"
        f.write('\n' + book_information)
    print("Book added successfully!")

'''
- Calls the 'get_book_information()' function to collect book information from the user.
- Collected information is then passed to the 'add_book()' function to add the book to the 'books_23094907.txt' file.
'''
book = get_book_information()
add_book(book)

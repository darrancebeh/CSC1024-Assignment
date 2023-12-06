'''
The 'datetime' module provides classes for manipulating dates and times in both simple and complex ways.
By importing the 'date' class, we can easily create and manipulate date objects in our code.
The "import traceback" statement allows us to handle and display error messages more effectively.
'''
from datetime import date
import traceback

'''
A function named 'add_book' that accepts 9 parameters (book details) as arguments.
'''


def add_book(isbn, author, title, publisher, genre, published_year, date_purchased, filename):
    try:
        with open(filename, 'a') as f:
            book_information = "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(
                isbn, author, title, publisher, genre, published_year, date_purchased, "Book's Status")
            f.write(book_information + '\n')
        print("Book added successfully!")
    except Exception as e:
        print("Error occurred: ", e, "\n", traceback.format_exc())


'''
A 'new_book_info' tuple that contains the book details to be added.
'''
new_book_info = ("1234567890123", "Author's Name", "Book's Title", "Publisher's Name",
                 "Genre of the Book", "2023", date(2023, 10, 10), "Book's Status")

'''
A call to the 'add_book' function, passing the book details as individual arguments using the * operator.
'''
add_book(*new_book_info, "books_23094907.txt")

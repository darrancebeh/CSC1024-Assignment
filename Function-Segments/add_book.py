import traceback
from datetime import date

    '''
    The Book class is used to represent a book.
    '''
class Book:
    def __init__(self, isbn, author, title, publisher, genre, published_year, date_purchased, status):
        self.isbn = isbn
        self.author = author
        self.title = title
        self.publisher = publisher
        self.genre = genre
        self.published_year = published_year
        self.date_purchased = date_purchased
        self.status = status

    '''
    The add_book() function is used to add a book to the books_23094907.txt file.
    '''
def add_book(new_book):
    try:
        with open("books_23094907.txt", 'a') as f:
            book_information = "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(
                new_book.isbn, new_book.author, new_book.title, new_book.publisher, new_book.genre, new_book.published_year, new_book.date_purchased, new_book.status)
            f.write(book_information + '\n')
        print("Book added successfully!")
    except Exception as e:
        print("Error occurred: ", e, "\n", traceback.format_exc())

new_book = Book(isbn="1234567890123",
                author="Author's Name",
                title="Book's Title",
                publisher="Publisher's Name",
                genre="Genre of the Book",
                published_year="2023",
                date_purchased=date.strptime("10-10-2023", '%d-%m-%Y'),
                status="Book's Status")

add_book(new_book)

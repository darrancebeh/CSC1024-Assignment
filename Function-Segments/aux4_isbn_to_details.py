from get_books import get_books


def isbn_to_details(isbn):
    '''
    Takes in an ISBN and returns the book details.
    '''
    book_list = get_books()
    for book in book_list:
        book = book.split("|")
        if (isbn == book[0]):
            return book

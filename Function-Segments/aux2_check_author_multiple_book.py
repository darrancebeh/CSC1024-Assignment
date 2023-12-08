from aux1_get_books import get_books


def check_author_multiple_book(author):
    '''
    Given author name, checks if author has multiple books in database.
    If author has multiple books, return list of all books of author.
    Else, return False.
    '''
    book_list = get_books()
    author_book_list = []
    for book in book_list:
        book_details = book.split("|")
        if (book_details[1] == author):
            author_book_list.append(book_details)

    if (len(author_book_list) > 1):
        return author_book_list
    else:
        return False

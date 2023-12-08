from aux1_get_books import get_books


def update_book(old_detail, new_detail, detail_type):
    '''
    Opens book database in write mode and replaces old details with new details.
    We use ISBN to identify which item to update.
    '''

    '''
    We use a dictionary to determine which index to replace based on the detail type.
    '''

    detail_to_index_identifier = {
        "isbn": 0,
        "author": 1,
        "title": 2,
        "publisher": 3,
        "genre": 4,
        "yop": 5,
        "dop": 6,
        "status": 7
    }

    book_list = get_books()

    for book in book_list:

        '''
        Finds the specific book to update.
        Updates the book details based on the detail type.
        Note that we use the detail_to_index_identifier dictionary to determine which index to replace.
        New details are updated in the book_list.
        '''

        book_details = book.split("|")
        if (book_details[detail_to_index_identifier[detail_type]] == old_detail):
            book_details[detail_to_index_identifier[detail_type]] = new_detail
            book_list[book_list.index(book)] = "|".join(book_details)

    '''
    Opens book database in write mode and writes the updated book list, replacing the old book list.
    '''

    with open("books_23094907.txt", "w") as f:
        f.write("\n".join(book_list))

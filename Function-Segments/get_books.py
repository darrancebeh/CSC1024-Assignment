def get_books():
    """
    Returns a list of all books in the database.
    """

    with open("books_23094907.txt", "r") as f:
        '''
        Returns all lines contained in the text file and separates every list item by line.
        '''
        book_list = f.read().split("\n")
        return book_list

def get_books():
    """
    Returns a list of all books in the database.
    """

    with open("books_23094907.txt", "r") as f:
        books = f.read().split("\n")

def update_book(old, new, book_list):
    '''
    Opens book database in write mode and replaces old details with new details.
    '''
    with open("books_23094907.txt", "w") as f:
        for book in book_list:
            if old in book:
                f.write(new + "\n")
            else:
                f.write(book + "\n")

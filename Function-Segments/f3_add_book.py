'''
- The 'def check_isbn_duplicate(isbn)' checks existing ISBNs. 
- It checks books_23094907.txt in read mode for similarities. 
'''


def check_isbn_duplicate(isbn):
    with open("books_23094907.txt", 'r') as f:
        for line in f:
            if line.split('|')[0] == isbn:
                return True
    return False


'''
- The 'def add_book(book)' function inserts the accepted details into books_23094907.txt in a specific format.
- Print out "Book added successfully!" if it's successful.
'''


def add_book(book_details):
    isbn, author, title, publisher, genre, published_year, date_purchased_str, status = book_details
    if '|' in title or '|' in author or '|' in publisher or '|' in genre:
        print(
            "Error: The character '|' is not allowed in the book's title, author's name, publisher's name and genre.")
        return
    else:
        book_information = f"{isbn}|{author}|{title}|{publisher}|{genre}|{published_year}|{date_purchased_str}|{status}"
        with open("books_23094907.txt", 'a') as f:
            f.write('\n' + book_information)
    print("Book added successfully!")


'''
- Calls the 'add_book_information()' function to collect book information from the user.
- Collected information is then passed to the 'add_book()' function to add the book to the 'books_23094907.txt' file.
'''

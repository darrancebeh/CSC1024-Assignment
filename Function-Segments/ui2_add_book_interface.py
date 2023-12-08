from datetime import datetime


def get_book_information():
    print("Please enter the following information:")
    while True:
        isbn = input("ISBN number: ")
        if len(isbn) == 13:
            if book_exists(isbn):
                print("Unsuccessful. Book already exists.")
                return None
            break
        else:
            print("Error. ISBN number must be 13 digits long. Please try again.")
    author = input("Author's name: ")
    title = input("Book's title: ")
    publisher = input("Publisher's name: ")
    genre = input("Genre of the book: ")
    while True:
        published_year = input("Publishing year: ")
        if published_year.isdigit() and int(published_year) > 0 and int(published_year) <= datetime.now().year:
            break
        else:
            print(
                "Error. Publishing year must be a positive integer and not in the future. Please try again.")
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
    status = input("Book's status: ")

    return isbn, author, title, publisher, genre, published_year, date_purchased_str, status


def book_exists(isbn):
    with open("books_23094907.txt", 'r') as f:
        for line in f:
            if line.split('|')[0] == isbn:
                return True
    return False


def add_book(book):
    if book is not None:
        with open("books_23094907.txt", 'a') as f:
            isbn, author, title, publisher, genre, published_year, date_purchased_str, status = book
            book_information = f"{isbn}|{author}|{title}|{publisher}|{
                genre}|{published_year}|{date_purchased_str}|{status}"
            f.write(book_information + '\n')
        print("Book added successfully!")


# Example usage:
book = get_book_information()
if book is not None:
    add_book(book)

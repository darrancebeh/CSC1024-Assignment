from datetime import date

'''
These lines of codes allows users to add books by inputting various details about the book, such as its ISBN number, author, title, publisher, genre, published year, date purchased and the current status of the book.
'''
def add_book():
    with open("books_23094907.txt", 'a') as f:
        print("Please enter the following information:")
        while True:
            isbn = input("ISBN number: ")
            if len(isbn) == 13:
                break
            else:
                print("Error. ISBN number must be 13 digits long. Please try again.")
        author = input("Author's name: ")
        title = input("Book's title: ")
        publisher = input("Publisher's name: ")
        genre = input("Genre of the book: ")
        published_year = input("Publishing year: ")
        date_purchased_str = input("Date purchased in the format DD-MM-YYYY: ")
        date_purchased = date.strptime(date_purchased_str, '%d-%m-%Y')
        status = input("Book's status: ")

        '''
        This line of code formats the book informations into a specific format.
        '''
        book_information = f"{isbn}\t\t{author}\t\t{title}\t\t{publisher}\t\t{status}"
        
        '''
        This line of code writes the book information to the books_23094907.txt file.
        '''
        f.write(book_information + '\n')

    print("Book added successfully!")

'''
This line of code calls the function.
'''
add_book()

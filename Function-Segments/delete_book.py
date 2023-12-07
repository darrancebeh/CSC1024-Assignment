
from get_books import get_books

def delete_book():
    '''
    Deletes books from the book list based on user input.
    This function utilizes a previously defined function get_books to retrieve the
    list of books from the database. It then prompts the user to enter information
    about the book they want to delete. The function removes books from the list
    containing the specified information and updates the original list.
    '''
    book_list = get_books()

    while True:
        # Display all books
        print("Current Book List:")
        for book in book_list:
            print(book)

        # Prompt user for input of isbn, author, or title for the book they want to delete
        search_book = input("Enter ISBN, author, or title of the book you want to delete: ")

        # Error handling for isbn/author/title input
        if not search_book:
            print("Invalid input. Please enter ISBN, author, or title.")
            continue

        # Use list comprehension to create a new list without the matching items
        filtered_book_list = [book for book in book_list if search_book.lower() not in book.lower()]

        if filtered_book_list != book_list:
            print(f"The information '{search_book}' was present in the following books and has been removed:")
            for item in book_list:
                if item not in filtered_book_list:
                    print(item)

            # Update the original list with the filtered list
            book_list = filtered_book_list
        else:
            print(f"The information '{search_book}' is not present in any of the books.")

        # Ask the user whether they want to delete another book
        another_deletion = input("Do you want to delete another book? (yes/no): ").lower()
        if another_deletion != 'yes':
            break

    print("Updated Book List:")
    for book in book_list:
        print(book)

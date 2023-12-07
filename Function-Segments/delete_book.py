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

    search_book = input("Enter book information: ")

    # Use list comprehension to create a new list without the matching items
    filtered_book_list = [book for book in book_list if search_book not in book]

    if filtered_book_list != book_list:
        print(f"The character '{search_book}' was present in the following books and has been removed:")
        for index, item in enumerate(book_list):
            if item not in filtered_book_list:
                print(f"Index {index}: {item}")

        book_list = filtered_book_list  # Update the original list with the filtered list
    else:
        print(f"The character '{search_book}' is not present in any of the books.")

    print("Updated Book List:", book_list)

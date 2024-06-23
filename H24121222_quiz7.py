library = {}

def add_book():
    """
    Prompts the user to enter the title, genre, and price of a book separated by vertical bars.
    Adds the book to the library dictionary with the title as the key and the genre and price as the value.
    Prints a message indicating that the book has been added.
    Returns True to indicate that the book was successfully added.
    """
    book_info = input("Enter the book title, genre, and price separated by a vertical bar (|): ")
    print()
    try:
        title, genre, price = book_info.split('|')
        title = title.strip()
        genre = genre.strip()
        price = float(price.strip())
        library[title] = (genre, price)
        print(f"Added '{title}' to the library.")
        return True
    except ValueError:
        print("Error: Please enter the title, genre, and price separated by a vertical bar (|).")
        print()
        return False

def remove_book():
    """
    Prompts the user to enter the title of a book to remove.
    Removes the book from the library if it is found and prints a message indicating that the book has been removed.
    If the book is not found, prints an error message and returns False.
    Returns True if the book is successfully removed.
    """
    title = input("Enter the title of the book to remove: ").strip()
    print()
    if title in library:
        del library[title]
        print(f"Removed '{title}' from the library.")
        return True
    else:
        print(f"Error: Book '{title}' not found in the library.")
        print()
        return False

def get_book_info():
    """
    Prompts the user to enter the title of a book to get information about.
    Prints the title, genre, and price of the book if it is found in the library.
    If the book is not found, prints an error message.
    """
    title = input("Enter the title of the book: ").strip()
    print()
    if title in library:
        genre, price = library[title]
        print(f"Title: {title}")
        print(f"Genre: {genre}")
        print(f"Price: ${price:.1f}")
        print()
    else:
        print(f"Error: Book '{title}' not found in the library.")
        print()

def list_books():
    """
    Lists all books in the library in alphabetical order by title.
    If the library is empty, prints a message indicating that it is empty and returns False.
    Returns True if there are books in the library.
    """
    if not library:
        print("\nThe library is empty.\n")
        print()
        return False
    print()
    for title, (genre, price) in sorted(library.items()):
        print("%s (%s, $%.2f)" % (title, genre, price))
    print()
    return True

def list_books_by_genre():
    """
    Prompts the user to enter a genre to search for.
    Lists all books in the library that match the specified genre in alphabetical order by title.
    If no books are found in the specified genre, prints an error message and returns False.
    Returns True if at least one book is found in the specified genre.
    """
    genre = input("Enter the genre: ").strip()
    books_in_genre = {title: (g, price) for title, (g, price) in library.items() if g.lower() == genre.lower()}
    if books_in_genre:
        print()
        for title, (g, price) in sorted(books_in_genre.items()):
            print("%s (%s,$%.2f)" % (title,g, price))
        print()
        return True 
    else:
        print(f"No books found in the'{genre}'genre.")
        print()
        return False

while True:
    print("Menu:\n1. Add a book\n2. Remove a book\n3. Get book information\n4. List all books\n5. List books by genre\n6. Quit")
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_book_return = add_book()
        if add_book_return:
            list_books()
    elif choice == "2":
        remove_book_return = remove_book()
        if remove_book_return:
            list_books()
    elif choice == "3":
        get_book_info()
    elif choice == "4":
        list_books()
    elif choice == "5":
        list_books_by_genre()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

print("Goodbye!")

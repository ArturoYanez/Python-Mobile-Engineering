"""
Library Management System

This program allows users to search available books, register new genres,
apply for book loans, and exit the system. It uses a dictionary to store
book data with ISBN as keys and handles availability status updates.
"""

# Book data structure: ISBN as key, (title, author, availability_status)
books = {
    "ISBN13-9780316015816": ("The Hobbit",
                            "J.R.R. Tolkien",
                            True),
    "ISBN13-9780439023528": ("Harry Potter and the Sorcerer's Stone",
                            "J.K. Rowling",
                            True),
    "ISBN13-9780060550796": ("To Kill a Mockingbird",
                            "Harper Lee",
                            True),
    "ISBN13-9780345391802": ("1984",
                            "George Orwell",
                            False),
    "ISBN13-9780679733417": ("Pride and Prejudice",
                            "Jane Austen",
                            True),
    "ISBN13-9780060850499": ("The Catcher in the Rye",
                            "J.D. Salinger",
                            False),
    "ISBN13-9780451524935": ("Fahrenheit 451",
                            "Ray Bradbury",
                            True),
    "ISBN13-9780060249017": ("The Great Gatsby",
                            "F. Scott Fitzgerald",
                            False),
    "ISBN13-9780393300003": ("The Adventures of Huckleberry Finn",
                            "Mark Twain",
                            True),
    "ISBN13-9780143035117": ("One Hundred Years of Solitude",
                            "Gabriel García Márquez",
                            False)
}

# System menu options
options = {
    "1": "Search available books",
    "2": "Register new genre",
    "3": "Apply for book loan",
    "4": "Exit system"
}


registered_genres = {'Action'}


def show_menu():
    """Display the main menu options to the user."""
    print("""\nWelcome to The Bibliophile's Bazaar
    —
    What would you like to do?
    —""")
    for key, value in options.items():
        print(f'{key}: {value}')


def get_option():
    """Get and validate user input for menu selection.
    \nReturns:
        int: Validated user choice between 1-4
    """
    while True:

        try:
            option = int(input('\nSelect an option (1-4): '))
            if option < 1 or option > 4:
                print('Please enter a number between 1 and 4.')
                continue
            return option
        except ValueError:
            print('Invalid input. Please enter a numeric value.')


def check_availability(book_collection):
    """Identify available books in the icollection.
    \nArgs:
        Dictionary containing book data
    \nReturns:
        list: ISBN and details of available books
    """
    return [(isbn, book) for isbn, book in book_collection.items() if book[2]]


def display_available_books():
    """Show formatted list of all available books."""
    available_books = check_availability(books)
    print("""\nAvailable Books:
        *   *   *   *   *   *   *   *   *""")
    for isbn, book in available_books:
        print(f"""ISBN: {isbn}
Title: {book[0]}
Author: {book[1]}
--------------""")


def register_genre(existing_genres):
    """Register new book genre in the system.
    \nArgs:
        existing_genres (set): Currently registered genre
    \nReturns:
        set: Updated set of genres with new addition
    """
    while True:
        new_genre = input('\nEnter genre to register: ').strip().title()
        if not new_genre:
            print('Genre cannot be empty. Try again.')
            continue
        if new_genre in existing_genres:
            print(f'"{new_genre}" already exists. Please enter a new genre.')

            continue
            
        existing_genres.add(new_genre)
        print(f'Successfully registered "{new_genre}" genre.')
        return existing_genres


def process_loan():
    """Handle book loan process including ISBN validation and status update.
    \nReturns:
        str: Loan confirmation message or availability notice
    """
    print("""\nBook Loan Process:
    |
    !TIP: Select option 1 from the menu to see available books""")
    
    while True:
        isbn_input = input('\nEnter 13-digit ISBN (starting with 978): ').strip()
        # Validate ISBN format
        if (len(isbn_input) != 13 or not isbn_input.isdigit() or
            not isbn_input.startswith('978')):
            print('''\nInvalid ISBN format. Must be
                  <F11>ISBN13-numeric characters starting with 978.''')
            continue
        full_isbn = f'ISBN13-{isbn_input}'
        available_books = check_availability(books)
        # Check book availability
        for isbn, book in available_books:
            if isbn == full_isbn:
                # Update availability status
                updated_book = (book[0], book[1], False)
                books[isbn] = updated_book
                return f"""\nEnjoy your book:
------------------
ISBN: {isbn}
Title: {book[0]}
Author: {book[1]}
!Please return by the due date. Thank you!
------------------"""
        print('\nBook not available. Please check ISBN or try another title.')


# Main program flow
if __name__ == "__main__":
    while True:
        show_menu()
        choice = get_option()
        if choice == 1:
            display_available_books()
        elif choice == 2:
            registered_genres = register_genre(registered_genres)
            print(f'\nCurrent genres: {", ".join(sorted(registered_genres))}')
        elif choice == 3:
            loan_result = process_loan()
            print(loan_result)
        elif choice == 4:
            print('\nThank you for using The Bibliophile\'s Bazaar!')
            print('Credits: Kry0')
            break




# Managment System of Library
# Data of Books Structure
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

# Initialization Menu
options = {
  "1": "Search a books avaliable",
  "2": "Register a unique genre",
  "3": "Apply for a loan",
  "4": "Exit"
}


registered_genres = {'Action'}



def show_menu():
  print(''' Welcome to The Bibliophile's Bazar
    —
    What do you do?
    —''')
  for key, value in options.items():
    print(f'{key}- {value}')


def get_option():
  while True:
    try:
        option = int(input('Select an option (1-4):'))
      if option < 0 :
        print('Negative numbers are not allowed, try again.')
        continue
      is_valid = lambda option: str(option) in options.keys()
      if is_valid(option):
        return option
      else:
        print('Invalid option try again.')
    except ValueError:
        print('Invalid type option, please try again')
        continue


def check_availability(books):
    availables = [
        (isbn, book) for isbn, book in books.items()if book[2] is True
        ]
    return availables

    
    
def search_available_books():
    availables = check_availability(books)
    print('''List of avaliables books:
        *   *   *   *   *   *   *   *   *''')
    for isbn, book in availables:
        print(f"""ISBN: {isbn}
name: {book[0]}
author: {book[1]}
--------------
""")


def register_genres(registered_genres):
    while True:

        try:
            registered_genres.add(str(input('Enter the genre to register: ')) break
        except KeyError:
            print('This genre already exists, please enter another one.')
            registered_genres.add(str(input('Enter the genre to register: '))
            
    print(registered_genres)
    
    

        genre = input('Enter the genre to register: ').strip().title()
        if genre in registered_genres:
            print(f'Error: {genre} already exits. Please enter a new genre.')
        else:
            registered_genres.add(genre)
            print(f'Genre {genre} added successfully.')
            break


def books_loan():
    while True:

        try:
            isbn_int = int(input('''Enter the code ISBN of the book: 
          |  
        ! if you dont know the ISBN code:
        try to select option 1 in menu for seem
        available books list'''))

        except ValueError:
            raise('ValieError: Invalid type input enter... Try again')
            continue
        isbn = str(isbn_int)

        if isbn[0:3] == '978' and len(isbn) == 13:
            isbn_validated = 'ISBN13'+'-'+isbn
            availables = check_availability(books)
            for i in availables:
                if i[0] == isbn_validated:
                    title, author, available = i[1]
                    available = False
                    books.update({isbn_validated: (title, author, available)})
                    return f''' Enjoy your book:
------------------
ISBN: {i[0]}
Title: {title}
Author: {author}
! REMEMBER RETURN ON TIME, Thanks you
------------------'''
            else:
                print('''------------------
This book is not available. Try with another book
------------------''')
                continue
        else:
            print('''------------------
            ISBN13 Code Invalid. Try again.
Tips: Must begin with 978 and have 13 characters
------------------''')
            continue



show_menu()

action = get_option()

if action == 1:
    search_available_books()
elif action == 2:

    register_genres(registered_genres)
    print(registered_genres)
elif action == 3:
    print(books_loan())
elif action == 4: 
    print('GoodBye - Credits to: Kry0')


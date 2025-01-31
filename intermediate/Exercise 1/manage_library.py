# Managment System of Library
# Data of Books Structure
books = {
    "ISBN13-9780316015816": ("The Hobbit", "J.R.R. Tolkien", True),
    "ISBN13-9780439023528": ("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", False),
    "ISBN13-9780060550796": ("To Kill a Mockingbird", "Harper Lee", True),
    "ISBN13-9780345391802": ("1984", "George Orwell", False),
    "ISBN13-9780679733417": ("Pride and Prejudice", "Jane Austen", True),
    "ISBN13-9780060850499": ("The Catcher in the Rye", "J.D. Salinger", False),
    "ISBN13-9780451524935": ("Fahrenheit 451", "Ray Bradbury", True),
    "ISBN13-9780060249017": ("The Great Gatsby", "F. Scott Fitzgerald", False),
    "ISBN13-9780393300003": ("The Adventures of Huckleberry Finn", "Mark Twain", True),
    "ISBN13-9780143035117": ("One Hundred Years of Solitude", "Gabriel García Márquez", False)
}

# Initialization Menu
options = {
  "1" : "Search a books avaliable",
  "2" : "Register a unique genre",
  "3" : "Apply for a loan",
  "4" : "Exit"
}
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
    except:
      print('Invalid type option... please try again')
      continue
    
show_menu()
get_option()
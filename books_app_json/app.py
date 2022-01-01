from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """

def menu():
    database.create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == "a":
            adding()
        elif user_input == "l":
            listing()
        elif user_input == "r":
            marking()
        elif user_input == "d":
            deleting()
        else:
            print("Please enter one of the letters listed above.")

        user_input = input(USER_CHOICE)

def adding():
    name = input('Enter the book title: ')
    author = input("Enter the book's author: ")

    database.add_book(name, author)

def listing():
    books = database.list_books()
    for book in books:
        read = 'YES' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']}, read: {read}")

def marking():
    name = input('Enter the title of a book you just read: ')

    database.mark_read(name)

def deleting():
    name = input('Enter the title of a book you want to delete: ')

    database.delete(name)


menu()
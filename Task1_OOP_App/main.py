from system import LibrarySystem
from utils import print_menu

library = LibrarySystem()

while True:
    print_menu()
    choice = input("Choose: ")

    if choice == "1":
        book = input("Book name: ")
        library.add_book(book)

    elif choice == "2":
        library.show_books()

    elif choice == "3":
        break

class Book:
    def __init__(self, title, author, quantity):
        self.title = title
        self.author = author
        self.quantity = quantity

class LibrarySystem:
    def __init__(self):
        self.library = {}

    def run(self):
        while True:
            self.print_menu()
            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.add_books()
            elif choice == 2:
                self.borrow_books()
            elif choice == 3:
                self.return_books()
            elif choice == 4:
                print("Exiting the program...")
                break
            else:
                print("Invalid choice. Please try again.")

            print()  # Print a newline for better formatting

    def print_menu(self):
        print("Library System Menu")
        print("1. Add Books")
        print("2. Borrow Books")
        print("3. Return Books")
        print("4. Exit")

    def add_books(self):
        title = input("Enter the book title: ")
        author = input("Enter the book author: ")
        quantity = int(input("Enter the quantity: "))

        if title in self.library:
            self.library[title].quantity += quantity
            print(f"Quantity updated for book: {title}")
        else:
            book = Book(title, author, quantity)
            self.library[title] = book
            print(f"Book added to the library: {title}")

    def borrow_books(self):
        title = input("Enter the book title: ")
        quantity = int(input("Enter the number of books to borrow: "))

        if title in self.library:
            book = self.library[title]
            if book.quantity >= quantity:
                book.quantity -= quantity
                print(f"Successfully borrowed {quantity} books: {title}")
            else:
                print(f"Insufficient quantity. Cannot borrow {quantity} books: {title}")
        else:
            print(f"Book not found in the library: {title}")

    def return_books(self):
        title = input("Enter the book title: ")
        quantity = int(input("Enter the number of books to return: "))

        if title in self.library:
            book = self.library[title]
            book.quantity += quantity
            print(f"Successfully returned {quantity} books: {title}")
        else:
            print(f"Book not found in the library: {title}")


# Main method to run the program
if __name__ == "__main__":
    library_system = LibrarySystem()
    library_system.run()

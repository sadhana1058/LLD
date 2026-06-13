class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def mark_checked_out(self):
        self.available = False

class Section:
    def __init__(self, name):
        self.name = name
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def checkout_book(self,title):
        for book in self._books:
            if book.title == title:
                if book.available:
                    book.mark_checked_out()
                    return True
                else:
                    return False
        return False

    # TODO: Add a checkout_book(title) method that returns bool
    # - Search through this section's books for a matching title
    # - If found AND available, mark it as checked out and return True
    # - If not found or already checked out, return False

class Library:
    def __init__(self):
        self._sections = []

    def add_section(self, section):
        self._sections.append(section)
    def checkout_book(self, title):
        for section in self._sections:
            if section.checkout_book(title):
                return True
        return False

    # TODO: Add a checkout_book(title) method that returns bool
    # - Iterate through all sections and delegate to each section's checkout_book()
    # - Return True as soon as any section successfully checks out the book
    # - Return False if no section has the book or it's unavailable
    # - CheckoutService should only need to call this single method

class CheckoutService:
    def __init__(self, library):
        self._library = library

    def checkout(self, book_title):
        # TODO: Replace with a single call to library's checkout_book() method
        # This method should be one line - no direct access to sections or books
        return self._library.checkout_book(book_title)

if __name__ == "__main__":
    library = Library()

    fiction = Section("Fiction")
    fiction.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))
    fiction.add_book(Book("1984", "George Orwell"))
    library.add_section(fiction)

    non_fiction = Section("Non-Fiction")
    non_fiction.add_book(Book("Clean Code", "Robert C. Martin"))
    library.add_section(non_fiction)

    service = CheckoutService(library)

    result1 = service.checkout("The Great Gatsby")
    print(f'Checking out "The Great Gatsby"... {"Success!" if result1 else "Failed (not found)"}')

    result2 = service.checkout("The Great Gatsby")
    print(f'Checking out "The Great Gatsby"... {"Success!" if result2 else "Failed (already checked out)"}')

    result3 = service.checkout("Unknown Book")
    print(f'Checking out "Unknown Book"... {"Success!" if result3 else "Failed (not found)"}')
# query_samples.py
from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        for book in books:
            print(f"Title: {book.title}, Author: {book.author.name}")
    except Author.DoesNotExist:
        print(f"No author found with the name {author_name}")

# List all books in a specific library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        for book in books:
            print(f"Title: {book.title}, Author: {book.author.name}")
    except Library.DoesNotExist:
        print(f"No library found with the name {library_name}")

# Retrieve the librarian for a specific library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        print(f"Librarian: {librarian.name} for Library: {library.name}")
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        print(f"Librarian or library not found for {library_name}")

# Example usage
if __name__ == "__main__":
    get_books_by_author("Author Name")          # Replace with actual author name
    get_books_in_library("Library Name")        # Replace with actual library name
    get_librarian_for_library("Library Name")   # Replace with actual library name

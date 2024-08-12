# Create a Book instance
```python
from bookshelf.models import Book
#comman to creat a Book instence
book =  Book(title = "1984", author = "George Orwell", publication_year = 1949)
book.save()
print(book.title, book.author, book.publication_year)
# Expected Output:
# 1984 George Orwell 1949
```
# Retrieve the Book instance
```python
from bookshelf.models import Book
# Command to retrieve and display all attributes of the Book instance
book = Book.objects.get(id = 1)
print(book.title, book.author, book.publication_year)
# Expected Output:
# 1984 George Orwell 1949
```
# Upate the book title
```python
from  bookshelf.models import Book

retrieved_book = Book.objects.get(title="1984")
# Command to upate the title of book
retrieved_book.title = "Nineteen Eighty-Four”
retrieved_book.save()
print(retrieved_book.titel)
# Expected output
#Nineteen Eighty-Four
```
# Delete the book instence
```python
from bookshelf.models import Book
# Delete the Book instance
retrived_book = Book.objects.get(id = 1)

book.delete()
# Command to confirm the deletion
books = Book.objects.all()
print(books)

# Expected Output:
#[]
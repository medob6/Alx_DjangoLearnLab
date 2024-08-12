# Retrieve the Book instance
```python
from bookshelf.models import Book

# Command to retrieve and display all attributes of the Book instance
book = Book.objects.get(id = 1)
print(book.title, book.author, book.publication_year)
# Expected Output:
# 1984 George Orwell 1949


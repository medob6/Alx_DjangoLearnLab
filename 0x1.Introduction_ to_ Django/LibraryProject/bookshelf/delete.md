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
# Delete the Book

```python
from bookshelf.models import Book

# Retrieve the book you want to delete
retrieved_book = Book.objects.get(title="1984")

# Delete the book
retrieved_book.delete()

# Verify the deletion
all_books = Book.objects.all()
print(all_books)

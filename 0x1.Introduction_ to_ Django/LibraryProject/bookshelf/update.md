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
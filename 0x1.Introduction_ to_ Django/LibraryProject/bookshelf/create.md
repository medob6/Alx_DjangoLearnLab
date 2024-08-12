# Create a Book instance
```python
from bookshelf.models import Book
#comman to creat a Book instence
book =  Book.objects.create(title = "1984", author = "George Orwell", publication_year = 1949)
book.save()
print(book.title, book.author, book.publication_year)
# Expected Output:
# 1984 George Orwell 1949
from relationship_app.models import Author, Book, Library, Librarian

Author.objects.get(name=author_name)
Library = Library.objects.get(name=library_name)
books_in_library = Library.books.all()
objects.filter(author=author)
Librarian.objects.get(library=library)
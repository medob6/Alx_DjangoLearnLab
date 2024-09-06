from django.shortcuts import render
from .models import Book
from django.views.generic import DetailView

# Create your views here.

def list_books(request):
    books = Book.objects.all() #this is a query that returns all the books in the books table using 
    return render(request, 'list_books.html', {'books': books})

class BookDetailView(DetailView):
  """A class-based view for displaying details of a specific book."""
  model = Book
  template_name = 'books/book_detail.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)  # Get default context data
    book = self.get_object()  # Retrieve the current book instance
    # Add the average rating to the context data
    context['average_rating'] = book.get_average_rating() 

from django.shortcuts import render
from .models import Book , Library
from django.views.generic import DetailView

# Create your views here.

def list_books(request):
    books = Book.objects.all() #this is a query that returns all the books in the books table using 
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
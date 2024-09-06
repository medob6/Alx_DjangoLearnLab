from django.urls import path
from .views import list_books
from django.views.generic import DetailView
urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', DetailView.as_view(), name='library_detail'),
]
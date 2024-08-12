from django.contrib import admin
from .models import Book

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Customize the list display in the admin interface
    list_display = ('title', 'author', 'publication_year')

    # Add filters for author and publication year
    list_filter = ('author', 'publication_year')

    # Add search functionality for title and author
    search_fields = ('title', 'author')
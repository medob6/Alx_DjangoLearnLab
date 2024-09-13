from django.contrib import admin
from .models import Book , Author , Librarian , Library , UserProfile
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title' , 'author')
    search_fields = ('title', 'author')
    list_filter = ('author' ,)

    def mark_as_featured(self, request, queryset):
        queryset.update(featured=True)

admin.site.register(Book , BookAdmin)
admin.site.register(Author)
admin.site.register(Librarian)
admin.site.register(Library)
admin.site.register(UserProfile)


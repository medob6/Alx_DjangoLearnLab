from django.urls import path
from .views import list_books
from .views import LibraryDetailView, LoginView, LogoutView , admin_view , librarian_view , member_view , add_book , edit_book , delete_book
from . import views

urlpatterns = [
    path("books/", list_books, name="list_books"),
    path(
        "library/<int:pk>/",
        LibraryDetailView.as_view(template_name="relationship_app/library_detail.html"),
        name="library_detail",
    ),
    path(
        "login/",
        LoginView.as_view(),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(),
        name="logout",
    ),
    path(
        "register/",
        views.register.as_view(),
        name="register",
    ),
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
    path('add_book/', add_book, name='add_book'),
    path('edit_book/', edit_book, name='edit_book'),
    path('delete_book/', delete_book, name='delete_book'),
]

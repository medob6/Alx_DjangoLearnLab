# relationship_app/views.py
from django.contrib.auth import login as auth_login , logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth.decorators import permission_required , user_passes_test

# relationship_app/views.py
from django.shortcuts import render, redirect , get_object_or_404
from django.views import View
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import user_passes_test

# from .forms import BookForm
from .models import Book
from .models import Library
from .forms import BookForm

# Create your views here.


def list_books(request):
    books = (
        Book.objects.all()
    )  # this is a query that returns all the books in the books table using
    return render(request, "relationship_app/list_books.html", {"books": books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


# Custom LoginView
class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, "relationship_app/login.html", {"form": form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect("home")  # Redirect to a home page or dashboard
        return render(request, "relationship_app/login.html", {"form": form})


# Custom LogoutView
class LogoutView(View):
    def get(self, request):
        auth_logout(request)
        return redirect("login")  # Redirect to login page after logout


# regestration view
class register(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "relationship_app/register.html", {"form": form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("home")  # Redirect to a home page or dashboard
        return render(request, "relationship_app/register.html", {"form": form})

# home
def home(request):
    return render(request, 'relationship_app/home.html')


def is_admin(user):
    """
    Check if a user is an admin.

    Args:
        user (User): The user to check.

    Returns:
        bool: True if the user is an admin, False otherwise.
    """
    return user.userprofile.role == "Admin"



def is_librarian(user):
    return user.userprofile.role == "Librarian"


def is_member(user):
    return user.userprofile.role == "Member"


@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")


@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")

# Add Book View
@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

# Edit Book View
@permission_required('relationship_app.can_change_book')
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form, 'book': book})

# Delete Book View
@permission_required('relationship_app.can_delete_book')
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'delete_book.html', {'book': book})
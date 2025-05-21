from django.urls import reverse_lazy
from .models import Book, Author
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import BookForm, AuthorForm
from django.contrib.auth.mixins import  LoginRequiredMixin, PermissionRequiredMixin


class AuthorListView(ListView):
    model = Author
    template_name = 'library/authors_list.html'
    context_object_name = 'authors'


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'library/author_form.html'
    success_url = reverse_lazy("library:books_list")


class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'library/author_form.html'
    success_url = reverse_lazy("library:books_list")


class BooksListView(LoginRequiredMixin,PermissionRequiredMixin, ListView):
    model = Book
    template_name = 'library/books_list.html'
    context_object_name = 'books'
    permission_required = 'library.view_book'


class BookCreateView(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'library/books_form.html'
    success_url = reverse_lazy('library:books_list')
    permission_required = 'library.add_book'

class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'library/books_detail.html'
    context_object_name = 'book'


class BookUpdateView(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    model = Book
    fields = ['title', 'publication_date', 'author']
    template_name = 'library/books_form.html'
    success_url = reverse_lazy('library:books_list')
    permission_required = 'library.change_book'


class BookDeleteView(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    model = Book
    template_name = 'library/books_confirm_delete.html'
    success_url = reverse_lazy('library:books_list')
    permission_required = 'library.delete_book'

# def books_list(request):
#     books = Book.objects.all()
#     context = {'books': books}
#     return render(request, 'library/books_list.html', context)
#
# def books_detail(request, book_id):
#     books = Book.objects.get(id=book_id)
#     context = {'book': books}
#     return render(request, 'library/books_detail.html', context)

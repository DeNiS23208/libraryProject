from django.urls import path
from .views import BooksListView, BookDeleteView, BookCreateView, BookDetailView, BookUpdateView, AuthorCreateView, \
    AuthorUpdateView, AuthorListView

# from .views import books_list, books_detail

app_name = 'library'
urlpatterns = [
    path("author/", AuthorListView.as_view(), name='author_list'),
    path("author/new/", AuthorCreateView.as_view(), name='author_create'),
    path("author/update/<int:pk>/", AuthorUpdateView.as_view(), name='author_update'),
    path("books/", BooksListView.as_view(), name='books_list'),
    path("books/new/", BookCreateView.as_view(), name='book_create'),
    path("books/<int:pk>/", BookDetailView.as_view(), name='book_detail'),
    path("books/update/<int:pk>/", BookUpdateView.as_view(), name='book_update'),
    path("books/delete/<int:pk>/", BookDeleteView.as_view(), name='book_delete'),
    # path("books_list/", books_list, name='books_list'),
    # path("books_detail/<int:book_id>", books_detail, name='books_detail'),
]

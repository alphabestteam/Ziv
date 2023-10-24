from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookView.as_view(), name='create-get'),
    path('books/<int:id>/', views.BookView.as_view(), name='delete-update'),
    path('bookAge/<int:id>/', views.book_age, name='book-age'),
    path('booksByAuthor/<str:author_name>/', views.books_by_author, name='books-by-author'),
    path('bookSelector/<int:id>/', views.book_selector, name='book-selector'),
    path('authors/', views.CreateAuthorView.as_view(), name='create-author'),
    ]

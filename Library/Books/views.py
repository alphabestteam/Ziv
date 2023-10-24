from django.http import HttpResponse
from rest_framework import status
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.views import APIView


class BookView(APIView):

    def post(self, request):
        serialized_book = BookSerializer(data=request.data)
        if serialized_book.is_valid():
            serialized_book.save()
            return Response(serialized_book.data, status=status.HTTP_201_CREATED)
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        books = Book.objects.all()
        serialized_books = BookSerializer(books, many=True)
        return Response(serialized_books.data, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        book_record = get_object_or_404(Book, id=id)
        serializer = BookSerializer(book_record, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        book = get_object_or_404(Book, pk=id)
        book.delete()
        return Response(f"Book number {id} has been deleted", status=200)

@api_view(["GET"])
def book_age(request, id):
    if request.method == "GET":
        book = get_object_or_404(Book, id=id)
        current_year = datetime.now().year
        publication_year = book.publication_date.year
        book_age = current_year - publication_year
        return Response({"Book age": book_age}, status=status.HTTP_200_OK)
    else:
        return Response(
            {"Your HTTP request is not of type GET, your method is not allowed"},
            status=405,
        )
    
@api_view(["GET"])
def books_by_author(request, author_name):
    books = Book.objects.filter(authors__name__icontains=author_name)
    serialized_books = BookSerializer(books, many=True)
    return Response(serialized_books.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def book_selector(request, id):
    """
    Demonstrates 'select_related'
    Retrieves a book and its authors
    """
    book = Book.objects.prefetch_related('authors').get(id=id)
    serialized_book = BookSerializer(book)
    return Response(serialized_book.data, status=status.HTTP_200_OK)

#This does not work with Many to Many and therefore cannot be demonstrated
"""
@api_view(["GET"])
def book_selector(request, id):
    book = Book.objects.prefetch_related('authors').get(id=id)
    serialized_book = BookSerializer(book)
    return Response(serialized_book.data, status=status.HTTP_200_OK)
"""


class CreateAuthorView(APIView):
    def post(self, request):
        serialized_author = AuthorSerializer(data= request.data)
        if serialized_author.is_valid():
            serialized_author.save()
            return Response(serialized_author.data, status=status.HTTP_201_CREATED)
        



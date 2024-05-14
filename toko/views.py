from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from .models import Book, Author, Order
from .serializers import BookSerializer, AuthorSerializer, OrderSerializer

# Create your views here.
@api_view(['GET', 'POST']) # decorator
@permission_classes([permissions.AllowAny])
def Book_list(request, format=None):

    if request.method == 'GET':
        Book = Book.objects.all()
        serializer = BookSerializer(Book, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Book_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        Book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializer(Book)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BookSerializer(Book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST']) # decorator
@permission_classes([permissions.AllowAny])
def Mobil_list(request, format=None):

    if request.method == 'GET':
        Author = Author.objects.all()
        serializer = AuthorSerializer(Author, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Author_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        Author = Author.objects.get(pk=pk)
    except Author.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AuthorSerializer(Author)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AuthorSerializer(Author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST']) # decorator
@permission_classes([permissions.AllowAny])
def Order_list(request, format=None):

    if request.method == 'GET':
        Order = Order.objects.all()
        serializer = OrderSerializer(Order, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Order_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        Order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Order(Order)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Order(Order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BookDetail(APIView):
    """
    ambil data, edit atau hapus data
    """
    parser_classes = [permissions.AllowAny]
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        Pemesanan = self.get_object(pk)
        serializer = BookSerializer(Book)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        Book = self.get_object(pk)
        serializer = BookSerializer(Book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        Book = self.get_object(pk=pk)
        Book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AuthorDetail(APIView):
    """
    ambil data, edit atau hapus data
    """
    parser_classes = [permissions.AllowAny]
    def get_object(self, pk):
        try:
            return Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        Mobil = self.get_object(pk)
        serializer = AuthorSerializer(Author)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        Author = self.get_object(pk)
        serializer = AuthorSerializer(Author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        Author = self.get_object(pk=pk)
        Author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OrderDetail(APIView):
    """
    ambil data, edit atau hapus data
    """
    parser_classes = [permissions.AllowAny]
    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        Order = self.get_object(pk)
        serializer = OrderSerializer(Order)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        Order = self.get_object(pk)
        serializer = OrderSerializer(Order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        Order = self.get_object(pk=pk)
        Order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

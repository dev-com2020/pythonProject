from django.contrib.auth import authenticate
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK
from rest_framework.views import APIView

from .models import Book
from .serializers import BookSeralizer

class Login(APIView):

    def post(self, request):
        user = authenticate(username=request.data.get("username"), password=request.data.get("password"))
        if not user:
            return Response({'error': 'Dane są błędne lub użytkownik nie istnieje'}, status=HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=HTTP_200_OK)


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSeralizer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]



@api_view()
def first_api_view(request):
    num_books = Book.objects.count()
    return Response({"num_books": num_books})


@api_view()
def all_books(request):
    books = Book.objects.all()
    book_serializer = BookSeralizer(books, many=True)
    return Response(book_serializer.data)

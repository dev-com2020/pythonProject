from django import forms

from bookr.book_management.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author']


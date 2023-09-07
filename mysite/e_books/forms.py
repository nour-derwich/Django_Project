from django import forms
from .models import Book
from .models import Author
from .models import User


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','description','imgae','number_page','category','rating']
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name','notes','books']
class UserForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['username','email']
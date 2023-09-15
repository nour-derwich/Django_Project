from django import forms
from .models import Book
from .models import Author

from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User  # Specify the User model
        fields = ['username', 'email', 'password']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','description','image','number_page','category','rating']
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name','notes','books']


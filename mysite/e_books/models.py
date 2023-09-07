from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.urls import reverse





    
    
    # # Add ManyToMany relationship between User and Author
    # favorite_authors = models.ManyToManyField(Author, related_name="favorite_users")
    
    # # Add ManyToMany relationship between User and Book
    # favorite_books = models.ManyToManyField(Book, related_name="favorite_users")
    
    
class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default="testyhedcbfiehf")
    image = models.TextField(default="https://www.chappellegardensra.com/app/uploads/2023/01/book-club-1-2.jpg")
    number_page = models.IntegerField(default=100)
    category = models.CharField(max_length=255, default="Fiction")  # Add category attribute
    rating = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)  # Add rating attribute
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE,null=True, related_name="owned_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug=models.SlugField(unique=True , db_index=True)
    # def get_absolute_url(self):
    #     return reverse("book-detail",args=[self.id])
    def __str__(self):
        return f"{self.title}"
class Author(models.Model):
    name = models.CharField(max_length=255)
    notes = models.TextField()
    books = models.ManyToManyField(Book, related_name="author_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    slug=models.SlugField(unique=True , db_index=True)
    # def get_absolute_url_author(self):
    #     return reverse("author-detail",args=[self.id])
    def full_name(slef):
        return f"{slef.name}"
    def __str__(self):
        return self.full_name
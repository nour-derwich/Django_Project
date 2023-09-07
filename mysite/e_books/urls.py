from django.urls import path 
from . import views
urlpatterns=[
    path('register/', views.register, name='register'),

  path('dashborad', views.get_books, name='book_list'),
  path('add/book/', views.create_book, name='create_book'),
  path('show/book/<int:id>/', views.show_book, name='show_book'),
  path('update/book/<int:book_id>/', views.update, name='update_book'),
 path('delete/book/<int:book_id>/', views.delete, name='delete_book'),
  path('author', views.get_author, name='list_authors'),
  path('add/author/', views.create_author, name='create_author'),
 path('show/author/<int:id>/', views.show_author, name='show_author'),
path('update/author/<int:author_id>/', views.update_author, name='update_author'),
path('delete/author/<int:author_id>/', views.delete_author, name='delete_author'),
  

]
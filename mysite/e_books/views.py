from django.shortcuts import render , redirect ,get_object_or_404

# from django.http import HttpResponse
from .models import Book
from .forms import BookForm
from .forms import AuthorForm
from .models import Author
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('book_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def get_books(request):
    context = {"books": Book.objects.all()}	
    return render(request,'allBooks.html',context)

@login_required
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            image = form.cleaned_data['image']
            number_page = form.cleaned_data['number_page']
            category = form.cleaned_data['category']
            rating = form.cleaned_data['rating']
            owner = request.user
            Book.objects.create(title=title,description=description,image=image,number_page=number_page,category=category,
                                rating=rating,owner=owner)
            return redirect('book_list')  # Redirect to the view displaying all books
    else:
        form = BookForm()

    return render(request, 'allBooks.html', {'form': form})
@login_required
def show_book(request, id):
    book = get_object_or_404(Book, pk=id)
    
    see_all=Author.objects.all()

    context = {
        'book': book,
        
        'see_all':see_all
    }

    if request.method == 'POST':
        author_id = request.POST.get('author')
        if author_id:
            author = Author.objects.get(pk=author_id)
            book.authors.add(author) 
   
    # print("pgpl^gl^pglh",authors)

    return render(request, 'show_book.html',context)

@login_required
def update(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm(instance=book)

    return render(request, 'edit_book.html', {'book':book ,'form': form})
@login_required
def delete(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == 'POST':
        book.delete()
        return redirect('list_books')

    return render(request, 'delete_book.html', {'book': book})

##############auther
@login_required
def get_author(request):
    authors= Author.objects.all()
    for author in authors:
        author.num_books = author.books.all().count()
    return render(request,'allAuthor.html',{'authors':authors})
@login_required
def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            notes = form.cleaned_data['notes']
            books = form.cleaned_data['books']
            
            Author.objects.create(name=name,notes=notes,books=books)
            return redirect('list_authors')  # Redirect to the view displaying all books
    else:
        form = AuthorForm()

    return render(request, 'allAuthor.html', {'form': form})
@login_required
def show_author(request, id):
    author = get_object_or_404(Author, pk=id)
    all_books = Book.objects.all()
    if request.method == 'POST':
        book_id = request.POST.get('book')
        if book_id:
            book = Book.objects.get(pk=book_id)
            author.books.add(book)
    
 

    return render(request, 'show_author.html', {'author': author,'all_books': all_books})
@login_required
def update_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('list_authors')
    else:
        form = AuthorForm(instance=author)

    return render(request, 'updat_author.html', {'form': form })
@login_required
def delete_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)

    if request.method == 'POST':
        author.delete()
        return redirect('list_authers')

    return render(request, 'delete_author.html', {'author': author})
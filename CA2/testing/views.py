from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import ContactForm
from .models import Author, Book

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data['name'])
            return redirect('thanks')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form':form})

def home(request):
    return HttpResponse("Home Page")


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


def add_book(request):
    authors= Author.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        price = request.POST.get('price')
        in_stock = request.POST.get('in_stock')

        author = Author.objects.get(id=author_id)

        Book.objects.create(
            title = title,
            author=author,
            price=price if price else None,
            in_stock=True if in_stock else False
        )

        return redirect('book_list')
    
    return render(request, 'add_book.html', {'auhtors':authors})



def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'book_detail.html', {'book':book})


def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('book_list')

def update_book(request, id):
    book = get_object_or_404(Book, id=id)
    authors = Author.objects.all()

    if request.method == 'POST':
        book.title = request.POST.get('title')
        author_id = request.POST.get('author')
        book.author = Author.objects.get(id=author_id)

        price = request.POST.get('price')
        book.price = price if price else None

        book.in_stock = True if request.POST.get('in_stock') else False

        book.save()

        return redirect('book_list')
    

    return render(request, 'update_book.html', {
        'book':book,
        'authors':authors
    })


def set_theme(request):
    theme = request.GET.get('theme', 'dark')

    if theme not in ['light', 'dark']:
        theme='light'


    resp = redirect('home')
    resp.set_cookie('theme', theme, max_age=3600, httponly=True)
    return resp


def read_theme(request):
    theme = request.COOKIES.get('theme', 'light')
    return HttpResponse(f'Theme:{theme}')

def clear_theme(request):
    resp = redirect('home')
    resp.delete_cookie('theme')
    return resp

def home(request):
    theme = request.COOKIES.get('theme', 'light')
    return render(request, 'home.html', {'theme':theme})

# Create your views here.

def visit_counter(request):
    count = request.session.get('visits', 0)+1
    request.session['visits'] = count
    return HttpResponse(f'Visits: {count}')

def reset(request):
    request.session.flush()
    return HttpResponse('Cleared')
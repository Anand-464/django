from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Book
from .forms import BookForm

def book_home(request):
    book_list=Book.objects.all()
    return render(request,'home.html',{'book_list':book_list})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_home')
    else:
        form = BookForm()
    return render(request, 'create.html', {'form': form, 'title': 'Add Book'})

def book_update(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_home')
    else:
        form = BookForm(instance=book)
    return render(request, 'update.html', {'form': form})

def book_delete(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_home')
    
    return render(request, 'delete.html', {'book': book})

def book_list(request):
    books = Book.objects.all()
    paginator = Paginator(books, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'list.html', {'page_obj': page_obj})


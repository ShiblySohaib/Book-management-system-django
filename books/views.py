from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

def homepage(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = BookForm()
        return render(request, 'add_book.html', {'form': form})
    


def delete_book(request, id):
    book = Book.objects.get(id = id)
    if book:
        book.delete()
    return redirect('homepage')


def update_book(request, id):
    targetForm = Book.objects.get(id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=targetForm)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = BookForm(instance=targetForm)
        return render(request, 'add_book.html', {'form': form})
from django.shortcuts import render, get_object_or_404, redirect
from .forms import BookForm
from .models import Book
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.paginator import Paginator


# Create your views here.


@login_required(login_url=settings.LOGIN_URL)
def dashboard(request):
    context = {}
    return render(request, 'dashboard/dashboard.html', context)


@login_required
def book_list(request):
    books = Book.objects.filter(owner=request.user)
    paginator = Paginator(books, 5)  # Menampilkan 5 buku per halaman
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'dashboard/book_list.html', {'page_obj': page_obj})


@login_required
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.owner = request.user
            book.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'dashboard/book_form.html', {'form': form})


@login_required
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'dashboard/book_form.html', {'form': form})


@login_required
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk, owner=request.user)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'dashboard/book_confirm_delete.html', {'book': book})

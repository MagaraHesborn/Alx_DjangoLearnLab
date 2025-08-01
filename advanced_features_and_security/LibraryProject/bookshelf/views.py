from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, 'books/book_list.html', context)

def index(request):
    return HttpResponseRedirect('/admin/login/')


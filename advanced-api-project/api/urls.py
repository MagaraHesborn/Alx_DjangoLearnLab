from django.urls import path
from .views import ListView, DeleteView, CreateView, UpdateView, DetailView

urlpatterns = [
    path('books/', ListView.as_view(), name='book-list'),
    path('books/Detail/', DetailView.as_view(), name='book-detail'),
    path('books/create/', CreateView.as_view(), name='book-create'),
    path('books/update/', UpdateView.as_view(), name='book-update'),
    path('books/delete/', DeleteView.as_view(), name='book-delete'),
]

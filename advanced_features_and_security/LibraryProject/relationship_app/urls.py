from django.urls import path
from .views import list_books, LibraryDetailView, Register, LoginView, LogoutView, home_view

urlpatterns = [
    path('', home_view, name='home'), 
    path('books/', list_books, name='list_books'),
    path('library/', LibraryDetailView.as_view(), name='library_detail'),
    path('signup/', Register.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('views.register', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
]

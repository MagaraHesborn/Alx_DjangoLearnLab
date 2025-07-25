from django.urls import path
from .views import list_books, LibraryDetailView, SignUpView, CustomLogInView, CustomLogOutView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/', LibraryDetailView.as_view(), name='library_detail'),
    path('signup/', SignUpView.as_view(), name='signup'),
      path('login/', CustomLogInView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', CustomLogOutView.as_view(""), name='logout'),
]

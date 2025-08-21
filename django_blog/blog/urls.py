from django.urls import path
from .views import Register, BlogLoginView, BlogLogoutView, profile, home, posts
from .views import ListView, DeleteView, CreateView, DetailView, UpdateView

urlpatterns = [
    path('', home, name='home'),
    path('register/', Register.as_view(), name='register'),
    path('login/', BlogLoginView.as_view(), name='login'),
    path('logout/', BlogLogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('posts/', posts, name='posts'),

    path('posts/', ListView.as_view(), name='post-list'),
    path('posts/detail/', DetailView.as_view(), name='post-list'),
    path('posts/create/', CreateView.as_view(), name='post-list'),
    path('postsdelete//', DeleteView.as_view(), name='post-list'), 
    path('posts/update/', UpdateView.as_view(), name='post-list'),
]
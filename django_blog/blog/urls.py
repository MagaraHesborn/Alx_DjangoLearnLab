from django.urls import path
from .views import (
    Register, BlogLoginView, BlogLogoutView, profile, home, posts,
         ListView, DeleteView, CreateView, DetailView, UpdateView
) 


urlpatterns = [
    path('', home, name='home'),

#AUTH

    path('register/', Register.as_view(), name='register'),
    path('login/', BlogLoginView.as_view(), name='login'),
    path('logout/', BlogLogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('posts/', posts, name='posts'),


# POST

     path('post/', ListView.as_view(), name='post-list'),                # List all posts
    path('post/new/', CreateView.as_view(), name='post-create'),        # Create a new post
    path('post/<int:pk>/', DetailView.as_view(), name='post-detail'),   # Post details
    path('post/<int:pk>/update/', UpdateView.as_view(), name='post-update'),  # Update post
    path('post/<int:pk>/delete/', DeleteView.as_view(), name='post-delete'),  # Delete post
]
from django.urls import path
from .views import (
    Register, BlogLoginView, BlogLogoutView, profile, home, posts,
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView
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

    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

]
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

    path('post/', PostListView.as_view(), name='post-list'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

]
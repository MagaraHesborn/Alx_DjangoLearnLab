from django.urls import path
from .views import Register, BlogLoginView, BlogLogoutView, profile

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('login/', BlogLoginView.as_view(), name='login'),
    path('logout/', BlogLogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
]
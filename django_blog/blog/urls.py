from django.urls import path
from .views import Register, BlogLoginView, BlogLogoutView

urlpatterns = [
    path('signup/', Register.as_view(), name='signup'),
    path('login/', BlogLoginView.as_view(), name='login'),
    path('logout/', BlogLogoutView.as_view(), name='logout'),
]
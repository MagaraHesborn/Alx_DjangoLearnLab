from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView


class Register(CreateView):
    form_class = UserCreationForm()
    success_url = reverse_lazy
    template_name = 'blog/register.html'

    def form_invalid(self, form):
        response = super().form_valid(form)

        login(self.request, self.object)
        return response
    
class LoginView(LoginView):
    template_name = 'blog/login.html'

class LogoutView(LogoutView):
    next_page = 'login'

# Create your views here.

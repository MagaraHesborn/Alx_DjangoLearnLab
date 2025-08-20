from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required


class Register(CreateView):
    form_class = UserCreationForm()
    template_name = 'blog/register.html'
    success_url = reverse_lazy("login") 
   

    def form_valid(self, form):
        response = super().form_valid(form)

        login(self.request, self.object) 
        return response
    
class BlogLoginView(LoginView):
    template_name = 'blog/login.html'

class BlogLogoutView(LogoutView):
    next_page = 'login'

@login_required
def profile(request):
    return render(request, 'blog/profile.html')

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm

 
def home(request):
    return render(request, 'blog/home.html')

class Register(CreateView):
    form_class = UserCreationForm
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
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your profile has been updated successfully!")
            return redirect("profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        "u_form": u_form,
        "p_form": p_form
    }
    return render(request, "blog/profile.html", context)

# Create your views here.

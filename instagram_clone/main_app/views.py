from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate 
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the insta main app.")

# def register(request):
#     form = CreateUserForm()

#     if request.method == "POST":
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#         else:
#             print(form.errors)

#     context = {"form": form}

#     return render(request, 'main/register.html', context)
def register(request):
    form = CustomUserCreationForm()
    success_msg = None
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            success_msg = "Registration successful. Please login."
            return redirect('login')
        else:
            print(form.errors)
        
    return render(request, 'main/register.html', {'form': form, "success_msg": success_msg})

def loginPage(request):
    if request.method == "POST":
        print(request.POST)
        username =  request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password= password)
        if user is not None:
            login(request, user)
            print("user logged in")
            return redirect('register')
    context = {}
    return render(request, 'main/login.html', context)
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate 
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import EditProfileForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the insta main app.")

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
        print(user)
        if user is not None:
            login(request, user)
            print("user logged in")
            return redirect('edit_profile')
    context = {}
    return render(request, 'main/login.html', context)

def chat(request):
    return render(request, 'main/chat.html')

def logoutUser(request):
    logout(request)
    return redirect('login')


# def follow_user(request, user_id):
#     user_to_follow = get_object_or_404(User, id=user_id)
#     if not request.user.following.filter(id=user_id).exists():
#         Follow.objects.create(follower=request.user, following=user_to_follow)
#     return redirect('profile_page')

# def unfollow_user(request, user_id):
#     user_to_unfollow = get_object_or_404(User, id=user_id)
#     request.user.following.filter(id=user_id).delete()
#     return redirect('profile_page')
def followers_count(request):
    pass

@login_required
def profile_page(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'main/profile_page.html', {'user_profile': user_profile})

def nav(request):
    return render(request, 'main/navbar.html')

@login_required
def home(request):
    return render(request, 'main/home.html')


@login_required
def edit_profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            print("Edit successful.")
            return redirect('profile_page')  # Ensure 'profile_page' is the correct name of the profile page URL
    else:
        form = EditProfileForm(instance=user_profile)
    return render(request, 'main/edit_user.html', {'form': form,'user_profile': user_profile})


from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from main_app.models import UserProfile

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Mobile Number or Email'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Retype Password'}))

    class Meta:
        model = User
        fields = ['email', 'first_name', 'username', 'password1', 'password2']


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'bio', 'photo']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'bio': forms.Textarea(attrs={'placeholder': 'Bio'}),
            'photo': forms.FileInput(attrs={'placeholder': 'Profile Picture'}),
        }
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserData, Projects
from django.shortcuts import render




class UserForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}))
    class Meta:
        model = User
        fields = ('email','password1','password2','username')
        widgets = {
            "email": forms.TextInput(attrs={'placeholder': 'Email'}),
            "username": forms.TextInput(attrs={'placeholder': "Username"}),
        }


class UserLoginForm(AuthenticationForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    class Meta:
        model = User
        fields = ('username','password')
        widgets = {
            "username": forms.TextInput(attrs={'placeholder': "Username"}),
        }

def get_id(request):
    value = request.user.id
    return value
class UserChangeForm(forms.ModelForm):


    class Meta:
        model = UserData
        fields = ('Fullname','UserGitLink','UserGroup','UserAvatar')

        widgets = {
            'Fullname': forms.TextInput(attrs={'placeholder': "Fullname"}),
            'UserGitLink': forms.TextInput(attrs={'placeholder': "Git-Hub Link"}),
            'UserGroup': forms.TextInput(attrs={'placeholder': "Group"}),

        }

class CreateProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ('ProjectName', 'ProjectDescription','ProjectLink')
        widgets = {
            "ProjectName": forms.TextInput(attrs={'placeholder': 'Project name'}),
            "ProjectDescription": forms.TextInput(attrs={'placeholder': "Description"}),
            "ProjectLink": forms.URLInput(attrs={'placeholder':'GitHub project link'})
        }
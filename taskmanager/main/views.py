from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from.forms import *
from django.contrib.auth.mixins import  LoginRequiredMixin
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .tests import *


def analytics(request):
    return render(request, 'main/analytics.html')

def dashboard(request):
    return render(request,'main/dashboard.html')

def users(request):
    return render(request,'main/users.html')

def settings(request):
    return render(request,'main/settings.html')



def base(request):
    return render(request,'main/base.html')

def test(requset):
    return render(requset,'main/test.html')

def create(request):
    return render(request, 'main/create.html')

def login(request):
    return  render(request,'main/login.html')

class RegisterUser(CreateView):
    form_class = UserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     print(context.items())
    #     return dict(list(context.items()))

class LoginUser(LoginView):
    form_class = UserLoginForm
    template_name = 'main/login.html'

def LogoutUser(request):
    logout(request)
    return redirect('login')

class ChangeUser(CreateView):
    form_class = UserChangeForm
    template_name = 'main/users.html'


def ChangeUserF(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data['id'] = request.user.id
            print(data)

            return redirect('login')
    else:
        form = UserChangeForm
        data = 0
    return render(request, 'main/users.html', {'form': form, 'data': data})



def testable(request):
    Users = User.objects.all()
    return render(request, 'main/analytics.html',{'users':Users})

def redirectlogin(request):
    test_1()
    print('------')
    test_2()
    print('------')
    return redirect('login')
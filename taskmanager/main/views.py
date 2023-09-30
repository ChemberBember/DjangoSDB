from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from.forms import *
from django.contrib.auth.mixins import  LoginRequiredMixin
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .functions import *
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
            cldata = form.cleaned_data
            try:
                print(cldata['UserAvatar'])
                data = UserData()
                data.UserF = User.objects.get(id=request.user.id)

                data.UserGroup = cldata['UserGroup']
                data.UserGitLink = cldata['UserGitLink']
                data.Fullname = cldata['Fullname']
                data.Usernick = request.user.username
                data.save()
            except:
                print(cldata['UserAvatar'])
                my_model = get_object_or_404(UserData, pk=request.user.username)
                form = UserChangeForm(request.POST, instance=my_model)

                data = form
                data.UserF = User.objects.get(id=request.user.id)
                data.UserGroup = cldata['UserGroup']
                data.UserGitLink = cldata['UserGitLink']
                data.Fullname = cldata['Fullname']
                data.UserAvatar = request.FILES['UserAvatar']
                data.save()
            return redirect('users')
    else:
        try:
            userdata = UserData.objects.get(pk=request.user.username)
        except:
            userdata = 0

        form = UserChangeForm(request.POST)
        try:
            form.fields['UserGroup'].widget.attrs['value'] = userdata.UserGroup
            form.fields['UserGitLink'].widget.attrs['value'] = userdata.UserGitLink
            form.fields['Fullname'].widget.attrs['value'] = userdata.Fullname
            form.fields['UserAvatar'].widget.attrs['value'] = userdata.UserAvatar

        except:
            pass
        data = 0

    return render(request, 'main/users.html', {'form': form, 'data': data,'userdata' : userdata })


def AddProject(request):
    form = CreateProjectForm(request.POST)
    if request.method == 'POST':
        form = CreateProjectForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            project = Projects()
            project.Usernick = UserData.objects.get(pk = request.user.username)
            project.ProjectName = data['ProjectName']
            project.ProjectDescription = data['ProjectDescription']
            project.ProjectLink = data['ProjectLink']
            project.save()
            return redirect('analytics')
    return render(request,'main/dashboard.html',{'form':form})

def testable(request):
    projects = Projects.objects.all()
    userdata = UserData.objects

    return render(request, 'main/analytics.html',{'projects': projects, 'userdata': userdata})

def redirectlogin(request):

    return redirect('login')
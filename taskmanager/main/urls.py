from django.urls import path
from . import views
from .views import RegisterUser, LoginUser, LogoutUser,ChangeUser

urlpatterns = [
    path('analytics',views.testable,name = 'analytics'),
    path('login',LoginUser.as_view(), name = 'login'), 
    path('registration',RegisterUser.as_view(),name = 'registration'),
    path('logout',LogoutUser,name = 'logout'),
    path('base',views.base),
    path('test',views.test),
    path('dashboard',views.AddProject,name = 'dashboard'),
    path('users', views.ChangeUserF,name = 'users'),
    path('settings', views.settings),
    path('',views.redirectlogin)


]

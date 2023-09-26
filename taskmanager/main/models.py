from django.db import models
from django.contrib.auth.models import User



class UserData(models.Model):
    Usernick = models.CharField(primary_key=True, max_length=20,default='ERROR')
    UserF = models.ForeignKey(User, on_delete=models.CASCADE)
    Fullname = models.CharField(max_length=20, null = True)
    UserAvatar = models.ImageField(upload_to='./templates/main/DBimages',null=True)
    UserGitLink = models.CharField(max_length=50, null = True)
    UserGroup = models.CharField(max_length=15, null = True)

class Projects(models.Model):
    UserF = models.ForeignKey(User, on_delete=models.CASCADE)
    ProjectName = models.CharField(max_length=100)
    ProjectDescription = models.TextField(null = True, blank = True,)
    ProjectLink = models.URLField(max_length=100)
    ProjectDate = models.DateTimeField(auto_now_add=True)
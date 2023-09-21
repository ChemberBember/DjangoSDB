from django.db import models
from django.contrib.auth.models import User



class UserData(models.Model):
    UserF = models.ForeignKey(User, on_delete=models.CASCADE)
    Fullname = models.CharField(max_length=20,null=True)
    UserAvatar = models.ImageField(upload_to='./templates/main/DBimages',null=True)
    UserGitLink = models.CharField(max_length=50,null=True)
    UserGroup = models.CharField(max_length=15,null=True)
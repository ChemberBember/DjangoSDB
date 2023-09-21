from django.contrib.auth.models import User
from .models import UserData


def test_1():
    Users = User.objects.all()

    for user in Users:
        print(dir(user))
        print(user.password)

def test_2():
    Objects = UserData.objects.all()

    for object in Objects:
        print(dir(object))
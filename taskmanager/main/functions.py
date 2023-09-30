from .models import UserData , Projects

def UserDataValues():
    print('#######################')
    projectdata = Projects.objects.values_list('ProjectName',"UserF_id")[0][0]
    print(projectdata)
    data = UserData.objects.values_list('Fullname',"UserF_id")
    return data
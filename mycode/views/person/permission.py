
from django.http import JsonResponse
from django.contrib.auth.models import User
import copy
data = []
data.append({"value": "1", "title": "添加装修公司", "disabled": "", "checked": ""})
data.append({"value": "2", "title": "添加建材市场", "disabled": "", "checked": ""})
data.append({"value": "3", "title": "添加设计师", "disabled": "", "checked": ""})

data.append({"value": "4", "title": "修改装修公司", "disabled": "", "checked": ""})
data.append({"value": "5", "title": "修改建材市场", "disabled": "", "checked": ""})
data.append({"value": "6", "title": "修改设计师", "disabled": "", "checked": ""})

data.append({"value": "7", "title": "删除装修公司", "disabled": "", "checked": ""})
data.append({"value": "8", "title": "删除建材市场", "disabled": "", "checked": ""})
data.append({"value": "9", "title": "删除设计师", "disabled": "", "checked": ""})

data.append({"value": "10", "title": "查看装修公司", "disabled": "", "checked": ""})
data.append({"value": "11", "title": "查看建材市场", "disabled": "", "checked": ""})
data.append({"value": "12", "title": "查看设计师", "disabled": "", "checked": ""})

group = []
group.append({"value": "1","title": "超级管理员","disabled": "","checked": ""})
group.append({"value": "2","title": "装修公司管理员","disabled": "","checked": ""})
group.append({"value": "3","title": "建材商家管理员","disabled": "","checked": ""})
group.append({"value": "4","title": "设计师管理员","disabled": "","checked": ""})

def getPermission(request):
    username = request.GET.get("username")
    print(username)
    user = User.objects.get(username=username)
    left = copy.deepcopy(data)
    right = []
    left2 = copy.deepcopy(group)
    right2 = []
    if user.has_perm('mycode.add_customer'):
        right.append(data[0])
    if user.has_perm('mycode.add_materials'):
        right.append(data[1])
    if user.has_perm('mycode.add_designer'):
        right.append(data[2])

    if user.has_perm('mycode.change_customer'):
        right.append(data[3])
    if user.has_perm('mycode.change_materials'):
        right.append(data[4])
    if user.has_perm('mycode.change_designer'):
        right.append(data[5])

    if user.has_perm('mycode.delete_customer'):
        right.append(data[6])
    if user.has_perm('mycode.delete_materials'):
        right.append(data[7])
    if user.has_perm('mycode.delete_designer'):
        right.append(data[8])

    if user.has_perm('mycode.view_customer'):
        right.append(data[9])
    if user.has_perm('mycode.view_materials'):
        right.append(data[10])
    if user.has_perm('mycode.view_designer'):
        right.append(data[11])

    if user.groups.filter(name='SuperAdmin').exists():
        right2.append(group[0])
    if user.groups.filter(name='customer').exists():
        right2.append(group[1])
    if user.groups.filter(name='materials').exists():
        right2.append(group[2])
    if user.groups.filter(name='designer').exists():
        right2.append(group[3])
    return JsonResponse({"data":[left,right,left2,right2]})



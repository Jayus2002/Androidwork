from django.http import JsonResponse
from django.contrib.auth import login
from django.contrib.auth.models import User
from mycode.models.customer.customer import Designer
import json
def registerSjs(request):
    if not request.user.has_perm('mycode.add_designer'):
        return JsonResponse({
            "result":"no_perm"
        })
    data = request.POST
    print(data)
    username = data.get("username"," ").strip()
    password = data.get("password"," ").strip()
    password_confirm = data.get("password_confirm","").strip()
    name = data.get("name")
    designerstyle = data.get("designerstyle")
    mobile = data.get("mobile")
    city = data.get("city")
    if not username or not password:
        return JsonResponse({
           'result':"zero"
            })
    if password != password_confirm:
        return JsonResponse({
            'result':"diffierent"
            })
    if User.objects.filter(username=username).exists():
        return JsonResponse({
            'result':"exist"
            })
    user = User(username=username)
    user.set_password(password)
    user.save()
    Designer.objects.create(user=user,username=user,name=name,mobile=mobile,city=city)
    return JsonResponse({
        'result':"success"
        })
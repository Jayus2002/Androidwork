from django.http import JsonResponse
from django.contrib.auth import login
from django.contrib.auth.models import User
from mycode.models.customer.customer import Customer
import json
def register(request):
    data = request.GET
    print(data)
    username = data.get("username"," ").strip()
    password = data.get("password"," ").strip()
    password_confirm = data.get("password_confirm","").strip()
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
    Customer.objects.create(user=user,username=user,name="default",mobile="123123123",city="asd",address="安徽省铜陵市")
    return JsonResponse({
        'result':"success"
        })


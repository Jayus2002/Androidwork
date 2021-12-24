from django.http import JsonResponse
from django.contrib.auth import authenticate, login

def signin(request):
#    if request.user.is_authenticated ():
#        return JsonResponse({
#            "result":"repeatLogin "
#            })
    if request.method =="POST":
        data = request.POST
    elif request.method == "GET":
        data = request.GET
#    print(data)
#    print(request.POST.get('loginUsername', 0))
    username = data.get('username')
    password = data.get('password')
    user = authenticate(username=username,password=password)
    if not user:
#        print("失败")
        return JsonResponse({
            "result":"false"
            })
    login(request,user)
#    print("成功")
    key = request.session.session_key
    return JsonResponse({
        "result":"success",
        "Cookie":key
        })

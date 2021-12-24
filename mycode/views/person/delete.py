from django.http import JsonResponse
from django.contrib.auth.models import User
tmp = []
def delete(request):
    data = request.GET
    tmp = data.getlist("user[]")
    print(tmp)
    for item in tmp:
#        print(item)
        this_object = User.objects.filter(username=item)
        this_object.delete()
    return JsonResponse({
        "result":"success"
    })
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.core import serializers
import json
def adminlist(request):
    if not request.user.is_authenticated:
        return JsonResponse({
            "result":"not_login"
            })
    this_object = User.objects.filter(is_staff=1)
    tmp = {}
    tmp['list'] = json.loads(serializers.serialize("json",this_object))
    data_back = []
    count = 0
    for item in tmp['list']:
        count = count + 1
        data_back.append(item['fields'])
    return JsonResponse({"code":0,"msg":"fuck","count":count,'data':data_back})


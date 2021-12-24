from django.http import JsonResponse
from mycode.models.customer.customer import Customer,Materials,Designer
from django.core import serializers
from django.contrib.auth.models import User
from django.db.models import Q
import json

def fuzzy_search(request):
    if not request.user.is_authenticated:
        return JsonResponse({
            "result":"not_login"
            })
    data = request.GET
    form = data.get('form')
    key = data.get('key')
    print(key)
    if form == "customer":
        this_object = Customer.objects.filter(Q(name__contains=key)|Q(city__contains=key)|Q(address__contains=key)|Q(mobile__contains=key))
    elif form == "materials":
        this_object = Materials.objects.filter(Q(name__contains=key)|Q(city__contains=key)|Q(address__contains=key)|Q(mobile__contains=key))
    elif form == "designer":
        this_object = Designer.objects.filter(Q(name__contains=key)|Q(city__contains=key)|Q(designstyle__contains=key)|Q(mobile__contains=key))
    elif form == "admin":
        this_object = User.objects.filter(Q(username__contains=key)).filter(is_staff=1)
    else:
        return JsonResponse({
            "result":"form_error"
            })
    tmp = {}
    tmp['list'] = json.loads(serializers.serialize("json",this_object))
    date_back = []
    count = 0
    for item in tmp['list']:
        count = count + 1
        date_back.append(item['fields'])
    return JsonResponse({"code":0,"msg":"fuck","count":count,'data':date_back})
#    tmp['list'] = json.loads(serializers.serialize("json",this_object))
#    print(tmp)
#    return JsonResponse({
#        "result":"FUCK!!!!!!!!!!!!!!"
#        })

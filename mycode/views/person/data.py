from django.http import JsonResponse
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from mycode.models.customer.customer import Customer,Materials,Designer
from django.core import serializers
import json

def data(request):
    if not request.user.is_authenticated:
        return JsonResponse({
            "result":"not_login"
            })
    print(request.user)
    this_data = request.GET
    form = this_data.get('form')
    if form == "customer":
        this_object = Customer.objects.all()
    elif form == "materials":
        this_object = Materials.objects.all()
    elif form == "designer":
        this_object = Designer.objects.all()
    else:
        return JsonResponse({
            "result":"form_error"
            })
    tmp = {}
    tmp['list'] = json.loads(serializers.serialize("json",this_object))
    date_back = []
    count = 0
    for item in tmp['list']:
        date_back.append(item['fields'])
        count = count + 1
    return JsonResponse({"code":0,"msg":"fuck","count":count,'data':date_back})

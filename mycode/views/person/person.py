from django.http import JsonResponse
from mycode.models.customer.customer import Customer,Materials,Designer
from django.core import serializers
from mycode.views.options import options
import json

def person(request):
    if not request.user.is_authenticated:
        print(request.session.get)
        return JsonResponse({
            "result":"not_login"
            })
    back = {}
    if request.method == "POST":
        data = request.POST
    else:
        data = request.GET
    username = request.user.get_username()
    if Customer.objects.filter(username=username).exists():
        this_object = Customer.objects.filter(username=username)
    else:
        if Materials.objects.filter(username=username).exists():
            this_object = Materials.objects.filter(username=username)
        else:
            if Designer.objects.filter(username=username).exists():
                this_object = Designer.objects.filter(username=username)
            else:
                return JsonResponse({
                    'result':"false"
                    })
    back['list'] = json.loads(serializers.serialize("json",this_object))
    print(back['list'][0]['fields'])
    return JsonResponse(back['list'][0]['fields'])

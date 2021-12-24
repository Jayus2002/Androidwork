from django.http import JsonResponse
from mycode.models.customer.customer import Customer,Materials,Designer
from django.core import serializers
from django.contrib.auth.models import User
import json
import random

def recommend(request):
    customer_index = Customer.objects.count() - 1
    materials_index = Materials.objects.count() - 1
    designer_index = Designer.objects.count() - 1
    index1 = random.randint(0, customer_index)
    index2 = random.randint(0, materials_index)
    index3 = random.randint(0, designer_index)
    print(index1)
    print(index2)
    print(index2)
    customer = Customer.objects.all()
    materials = Materials.objects.all()
    designer = Designer.objects.all()
    back = {}
    back['customer'] = json.loads(serializers.serialize("json",customer))
    back['materials'] = json.loads(serializers.serialize("json",materials))
    back['designer'] = json.loads(serializers.serialize("json",designer))
    res = {}
    res = {"customer":back['customer'][index1]['fields'],"materials":back['materials'][index2]['fields'],"designer":back['designer'][index3]['fields']}
    print(res)
    return JsonResponse(res)




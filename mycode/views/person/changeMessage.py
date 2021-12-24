from django.http import JsonResponse
from mycode.models.customer.customer import Customer,Materials,Designer

def changeMessage(request):
    data = request.POST
    print(data)
    username = data.get("username")
    newName = data.get("name")
    newMobile = data.get("mobile")
    newCity = data.get("city")
    if data.get("form")=="customer":
        this_object=Customer.objects.get(username=username)
        if not newName is None:
            if newName != "":
                this_object.name=newName
        if not newMobile is None:
            if newMobile != "":
                this_object.mobile = newMobile
        if not newCity is None:
            if newCity != "":
                this_object.city = newCity
        this_object.save()
    elif data.get("form")=="materials":
       
        this_object=Materials.objects.get(username=username)
        if not newName is None:
            if newName != "":
                this_object.name=newName
        if not newMobile is None:
            if newMobile != "":
                this_object.mobile = newMobile
        if not newCity is None:
            if newCity != "":
                this_object.city = newCity
        this_object.save()
    elif data.get("dorm")=="designer":
        this_object=Designer.objects.get(username=username)
        if not newName is None:
            if newName != "":
                this_object.name=newName
        if not newMobile is None:
            if newMobile != "":
                this_object.mobile = newMobile
        if not newCity is None:
            if newCity != "":
                this_object.city = newCity
        this_object.save()
    return JsonResponse({
        "result":"success"
    })

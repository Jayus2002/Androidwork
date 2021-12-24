from django.http import JsonResponse
from django.contrib.auth.models import User
from mycode.models.customer.customer import Customer
def person_change(request):
    if not request.user.is_authenticated:
        return JsonResponse({
            "result":"not_login"
            })
    username = request.user.get_username()
    data = request.GET
    newName = data.get("name")
    newAddress = data.get("address")
    newAllName = data.get("allName")
    newMobile = data.get("mobile")
    newLogo = data.get("logo")
    newCity = data.get("city")
    this_object = Customer.objects.get(username=username)
    if not newName is None:
        if newName != "":
            this_object.name=newName
    if not newAddress is None:
        if newAddress != "":
            this_object.address = newAddress
    if not newAllName is None:
        if newAllName != "":
            this_object.allName = newAllName
    if not newMobile is None:
        if newMobile != "":
            this_object.mobile = newMobile
    if not newLogo is None:
        if newLogo != "":
            this_object.logo = newLogo
    if not newCity is None:
        if newCity != "":
            this_object.city = newCity
    this_object.save()
    return JsonResponse({
        "result":"sucess"
        })
def person_delete(request):
    if not request.user.is_authenticated:
        return JsonResponse({
            "result":"not_login"
            })
    username = request.user.get_username()
    if username == "bcl":
        return JsonResponse({
        "result":"can_not_delete"
            })
    this_object = User.objects.get(username=username)
    this_object.delete()
    return JsonResponse({
        "result":"success"
        })


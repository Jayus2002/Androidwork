from django.http import JsonResponse

def judge_login(request):
    if request.user.is_authenticated:
        return JsonResponse({
            "result":"yes"
            })
    else:
        return JsonResponse({
            "result":"no"
            })

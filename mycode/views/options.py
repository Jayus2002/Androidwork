from django.http import JsonResponse

def options(request):
    method = request.META.get('Access-Control-Allow-Method')
    origin = request.META.get('Origin')
    response = Response()
    print("FUCK!!!!!!!!!!!!")
    response['Access-Control-Allow-Method'] = method
    response['Access-Control-Allow-Origin'] = "http://127.0.0.1:8848"
    response["Access-Control-Allow-Headers"] = "X-CSRFToken, Content-Type"
    return response

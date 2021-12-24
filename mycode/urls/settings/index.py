from django.urls import path,include
from mycode.views.settings.signin import signin
from mycode.views.settings.register import register
from mycode.views.settings.signout import signout
urlpatterns =[
    path("signin/",signin,name = "mycode.views.settings.signin"),
    path("register/",register,name="mycode.views.settings.register"),
    path("signout/",signout,name="mycode.views.settings.signout"),
    ]

from django.urls import path,include
from mycode.views.person.person import person
from mycode.views.person.person_change import person_change,person_delete
from mycode.views.person.data import data
from mycode.views.person.fuzzy_search import fuzzy_search
from mycode.views.person.adminlist import adminlist
from mycode.views.person.recommend import recommend
from mycode.views.person.judge_login import judge_login
from mycode.views.person.registerZx import registerZx
from mycode.views.person.registerJc import registerJc
from mycode.views.person.registerSjs import registerSjs
from mycode.views.person.delete import delete
from mycode.views.person.changeMessage import changeMessage
from mycode.views.person.permission import getPermission
urlpatterns = [
    path("person/",person,name = "mycode.views.person.person"),
    path("data/",data,name="mycode.views.person.data"),
    path("judge_login/",judge_login,name="mycode.views.person.judge_login"),
    path("adminlist/",adminlist,name="mycode.views.person.adminlist"),
    path("recommend/",recommend,name="mycode.views.person.recommend"),
    path("fuzzy_search/",fuzzy_search,name="mycode.views.person.fuzzy_search"),
    path("person_change/",person_change,name="mycode.views.person.person_change"),
    path("person_delete/",person_delete,name="mycode.views.person.person_delete"),
    path("registerZx/",registerZx,name="mycode.views.person.registerZx"),
    path("registerJc/",registerJc,name="mycode.views.person.registerJc"),
    path("registerSjs/",registerSjs,name="mycode.views.person.registerSjs"),
    path("delete/",delete,name="mycode.views.person.delete"),
    path("changeMessage/",changeMessage,name="mycode.views.person.changeMessage"),
    path("getPermission/",getPermission,name="mycode.views.person.getPermission"),
    ]

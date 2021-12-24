from django.urls import path,include

urlpatterns = [
    path("settings/", include("mycode.urls.settings.index")),
    path("person/",include("mycode.urls.person.index")),
]

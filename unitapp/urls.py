from django.urls import path
from .import views

urlpatterns =[
    path("",views.length,name="length"),
    path("weight/",views.weight,name="weight"),
    path("height/",views.height,name="height"),
]
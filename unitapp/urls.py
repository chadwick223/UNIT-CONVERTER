from django.urls import path
from .import views

urlpatterns =[
    path("",views.index,name="index"),
    path("length/",views.length,name="length"),
    path("weight/",views.weight,name="weight"),
    path("height/",views.height,name="height"),
]
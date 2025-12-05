from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from pint import UnitRegistry
from pint import UnitRegistry
ureg=UnitRegistry()
from .forms import inputform
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    result=None
    if request.method=="POST":
        value=float(request.method.POST.get("value"))
        result=print("waiting for result?")
        return render(request,length.html,)

def length(request):
    result=None
    if request.method=="POST":
        form=inputform(request.POST)
        if form.is_valid():
            value=form.cleaned_data["value"]
            from_unit=form.cleaned_data["Unit_to_convert_from"]
            to_unit=form.cleaned_data["Unit_to_convert_to"]

            quantity=value*ureg(from_unit)
            converted=quantity.to(to_unit)
            result=converted.magnitude
        else:
            pass
    
    else:
        form=inputform()
    return render(request,"unitapp/length.html",{"form": form, "result": result})
    
    #return HttpResponse("you're at length page")

def height(request):
    result=None
    if request.method=="POST":
        form=inputform(request.POST)

        if form.is_valid():
            value=form.cleaned_data["value"]
            from_unit=form.cleaned_data["Unit_to_convert_from"]
            to_unit=form.cleaned_data["Unit_to_convert_to"]

            quantity=value*ureg(from_unit)
            converted=quantity.to(to_unit)
            result=converted.magnitude
        else:
            pass
    else:
        form=inputform()

    return render(request,"unitapp/height.html",{"form":form,"result":result,})


@csrf_exempt
def weight(request):
    result=None

    if request.method=="POST":
        form=inputform(request.POST)

        if form.is_valid():
            value=form.cleaned_data["value"]
            from_unit=form.cleaned_data["Unit_to_convert_from"]
            to_unit=form.cleaned_data["Unit_to_convert_to"]

            quantity=value*ureg(from_unit)
            converted=quantity.to(to_unit)
            result=converted.magnitude
        else:
            pass
    else:
        form=inputform()

    return render(request,"unitapp/weight.html",{"form":form,"result":result,})
    
    #return HttpResponse("you're at length page")

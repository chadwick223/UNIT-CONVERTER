from django.shortcuts import render
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
    form=inputform()
    result=None
    if request.method=="POST":
        form=inputform(request.POST)
        value=float(request.POST.get("value"))
        result=print("somelogic")
    return render(request,"unitapp/length.html",{"form": form, "result": result})
    
    #return HttpResponse("you're at length page")

def height(request):
    form=inputform()
    result=None
    if request.method=="POST":
        form=inputform(request.POST)
        value=float(request.POST.get("value"))
        result=print("somelogic")
    return render(request,"unitapp/height.html",{"form":form,"result":result})
    
    #return HttpResponse("you're at length page")

@csrf_exempt
def weight(request):
    form=inputform()
    result=None
    if request.method=="POST":
        form=inputform(request.POST)
        if form.is_valid():
            value=form.cleaned_data["value"]
            unit_from=form.cleaned_data["Unit_to_convert_from"]
            unit_to=form.cleaned_data["unit_to_convert_to"]

            try:
                converted=(value*ureg(unit_from)).to(unit_to)
                result=f"{converted.magnitude} {converted.units}"
            except:
                result="Invalid units"
    return render(request,"unitapp/weight.html",{"form":form,"result":result})
    
    #return HttpResponse("you're at length page")

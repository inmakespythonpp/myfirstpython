# from django.shortcuts import render
from django.shortcuts import render

from .models import place, Team


# Create your views here.



def demo(request):
    obj=place.objects.all()
    ob=Team.objects.all()

    return render(request,"index.html",{'result':obj,'results':ob})












#def addition(request):
 #   x=int(request.GET['num1'])
 #   y=int(request.GET['num2'])
 #   res=x+y
 #   return render(request,"result.html",{'result':res})

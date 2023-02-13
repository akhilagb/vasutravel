from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Team
# Create your views here.
def home(request):
    # name="India"
    obj1=Place.objects.all()
    obj2= Team.objects.all()
    return render(request,"index.html",{'res1':obj1,'res2':obj2})
# def addition(request):
#     x=int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     res=x+y
#     return render(request,"result.html",{'result':res})
# def about(request):
#     return render(request,"about.html")
# def contact(request):
#     return render(request,"contact.html")
# def detail(request):
#     return render(request,"detail.html")
# def thanks(request):
#     return HttpResponse("Thanks")

from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")

def blr1(request):
    return render(request,"blr1.html")

def blr1pg2(request):
    return render(request,"blr1pg2.html")

def blr2(request):
    return render(request,"blr2.html")

def blr2pg2(request):
    return render(request,"blr2pg2.html")

def blr2pg3(request):
    return render(request,"blr2pg3.html")

def schedules(request):
    return render(request,"schedules.html")

def hyd(request):
    return render(request,"hyd.html")

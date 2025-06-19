from django.shortcuts import render,redirect
from .models import Contact
# Create your views here.

def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def projects(request):
    return render(request,"projects.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        msg = request.POST.get('message')
        if email and msg :
            user = Contact(name=name, email=email, message=msg)
            user.save()
            return redirect("success")
    return render(request,"contact.html")

def success(request):
    return render(request,"success.html")
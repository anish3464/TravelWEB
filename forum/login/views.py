from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.
def loginaction(request):
    if request.method=="POST":
        email = request.POST["email"]
        passw = request.POST["password"]
        print(request.POST)
        user = authenticate(username=email, password=passw)
        if not user:
            return render(request,'error.html')
        else:
            return render(request,"welcome.html")

    return render(request,'login_page.html')
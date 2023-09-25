from django.shortcuts import render
from django.contrib.auth.models import User
import mysql.connector as sql

# Create your views here.
def signaction(request):


    if request.method=="POST":
        items=request.POST
        # print(d)
        user = User.objects.create_user(items["first_name"] + items["last_name"], items["email"], items["password"])

        user.sex = items["sex"]

        user.save()

        return render(request, "login_page.html")

    elif request.method == "GET":
        return render(request,'signup_page.html')
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def signaction(request):


    if request.method=="POST":
        items=request.POST
        
        try:
            user = User.objects.create_user(
                username=items["first_name"] + items["last_name"], 
                email=items["email"], 
                password=items["password"]
            )
            user.first_name = items["first_name"]
            user.last_name = items["last_name"]
            user.save()
            
            messages.success(request, 'Account created successfully! Please log in.')
            return render(request, "login_page.html")
            
        except Exception as e:
            messages.error(request, 'Error creating account. Please try again.')
            return render(request, "signup_page.html")

    else:
        return render(request,'signup_page.html')
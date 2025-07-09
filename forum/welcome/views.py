from django.shortcuts import render
import os
from datetime import date
def welcome(request):
    return render(request,'welcome.html')
name=''
post=''

def post(request):
    global name,post
    if request.method=="POST":
        # For now, we'll just store the data in session or redirect
        # In a real application, you would save this to a database
        name = request.POST.get('first_name', '')
        post_content = request.POST.get('posht', '')
        
        # You can add database logic here later
        # For now, just redirect back to welcome page
        return render(request, 'welcome.html')
 
    return render(request,'community.html')

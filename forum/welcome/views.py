from django.shortcuts import render
import mysql.connector as sql
from datetime import date
def welcome(request):
    return render(request,'welcome.html')
name=''
post=''

def post(request):
    global name,post
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="asnasnasn",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="first_name":
                name=value
            if key=="posht":
                post=value
        c="insert into post Values('{}','{}','{}')".format(name,date.today(),post)
        cursor.execute(c)
        m.commit()
 
    return render(request,'community.html')

from django.contrib import admin
from django.urls import path
from signup.views import signaction
from login.views import loginaction
from welcome.views import welcome,post
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',signaction),
    path('login/',loginaction),
    path('welcome/',welcome),
    path('community/',post),
]
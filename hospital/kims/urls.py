from django.urls import path
from .views import *

urlpatterns = [
    path('',signup,name="signup"),
    path('login/',user_login,name="login"),
    path('logout/',user_logout,name="logout"),

    path('index/', index, name="index"),
    path('about/',about,name="about"),
    path('doctor/',doctor,name="doctor"),
    path('department/',department,name="department"),
    path('booking/',booking,name="booking"),
    path('contact/',contact,name="contact"),

]
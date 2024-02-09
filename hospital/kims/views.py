from django.shortcuts import render,redirect,HttpResponse
from .models import Department,Doctor,Booking
from .forms import BookingForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
# from django.contrib.auth import authenticate,login as log
from django.contrib.auth import logout


# Create your views here.

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")


# department     

def department(request):
    dict_dept = {
        'dept': Department.objects.all()
    }
    return render(request, 'department.html', dict_dept)


# doctor 

def doctor(request):
    docs = {
        'doc': Doctor.objects.all()
    }
    return render(request, 'doctor.html',docs)


# booking 

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Booking Added Successfully")
            # return render(request,'index.html')
        else :
            messages.warning(request, "Something went wrong!")
    form = BookingForm()
    dict_form = {
        'form' : form
    }
    return render(request,'booking.html',dict_form)

    


def contact(request):
    return render(request,"contact.html")


# signup 

def signup(request):
    if request.method=="POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        myuser = User.objects.create_user(username,email,password)
        myuser.save()
        return redirect('login')
    return render(request,'signup.html')

# login 

def user_login(request):
    if request.method == "POST":
        username1 = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username1, password=password)
        if user is not None:
            login(request,user)
            # return HttpResponse("LOGGED")
            return redirect("index")
        else:
            return redirect("signup")
    return render(request, 'login.html')

# logout

def user_logout(request):
    logout(request)
    return redirect("login")



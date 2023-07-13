from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request, "authentication/index.html")


def signup(request):
    if request.method == "POST":
        # username=request.POST.get("username")
        userName = request.POST['username']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password1']
        c_password = request.POST['password2']

        myuser = User.objects.create_user(userName, email, password)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "User Saved")

        return redirect("signin")

    return render(request, "authentication/signup.html")


def signin(request):
    return render(request, "authentication/signin.html")


def signout(request):
    return render(request, "authentication/signout.html")

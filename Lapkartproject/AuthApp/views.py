from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.
def register_view(request):
    if request.method == "POST":
        signup_form = UserCreationForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            return redirect("/auth/login/")
    template_name = "AuthApp/register.html"
    signup_form = UserCreationForm()
    context = {"signup_form":signup_form}
    return render(request, template_name, context)

def login_view(request):
    if request.method == "POST":
        u = request.POST["uname"]
        p = request.POST["pw"]
        print("u=",u,"p=",p)
        user = authenticate(username=u,password=p)
        if user is not None:
            login(request,user)
            return redirect("/seller/show/")
    template_name = "AuthApp/login.html"
    context = {}
    return render(request, template_name, context)

def logout_view(request):
    logout(request)
    return redirect("/auth/login/")


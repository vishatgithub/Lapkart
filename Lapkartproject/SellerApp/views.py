from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from.forms import LaptopForm
from.models import Laptop

# Create your views here.
def add_laptop(request):
    if request.method == "POST":
        form = LaptopForm(request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponse("laptop added")
            return redirect("/seller/show/")
    template_name = "SellerApp/add_laptop.html"
    form = LaptopForm()
    context = {"form":form}
    return render(request, template_name, context)
@login_required(login_url="/auth/login/")
def show_laptops(request):
    template_name = "SellerApp/show_laptops.html"
    laptop_obj = Laptop.objects.all()
    context = {"laptop_obj":laptop_obj}
    return render(request, template_name, context)

def update_laptop(request,i):
    lap_obj = Laptop.objects.get(id=i)
    if request.method == "POST":
        form = LaptopForm(request.POST,instance=lap_obj)
        if form.is_valid():
            form.save()
            return redirect("/seller/show/")
    template_name = "SellerApp/add_laptop.html"
    form = LaptopForm(instance=lap_obj)
    context = {"form":form}
    return render(request,template_name,context)

def delete_laptop(request,j):
    lap_obj = Laptop.objects.get(id=j)
    lap_obj.delete()
    return redirect("/seller/show/")

def home_view(request):
    template_name = "SellerApp/home.html"
    context={}
    return render(request, template_name, context)
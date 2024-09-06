from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    people = [
        {'name': 'afraj', 'age': 23},
        {'name': 'himanshu', 'age': 24},
        {'name': 'monis', 'age': 25},
        {'name': 'sahil', 'age': 26},
    ]
    return render(request,"home/index.html", context={'people':people})

def about(request):
    return render(request, "home/about.html")

def contact(request):
    return render(request, "home/contact.html")


def success_page(request):
    return HttpResponse("<h1>success page </h1>")

# Create your views here.

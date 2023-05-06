from django.shortcuts import render
from  django.http import  HttpResponse

# Create your views here.


def emp(request):
    return HttpResponse("---- welcome to employees page ")


def landingpage(request):
    return render(request, 'landing.html')

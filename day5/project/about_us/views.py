from django.shortcuts import render
from  django.http import  HttpResponse

# Create your views here.


def go_aboutus(request):
    return HttpResponse("---- welcome to about us page ")
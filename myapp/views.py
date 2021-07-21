from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from django.http import  HttpResponse 

def index(request):
    return HttpResponse('<h1 style="text-align:center">The Home Page!</h1><br>  <img src="https://image.shutterstock.com/image-photo/gadgets-accessories-isolated-on-white-260nw-1248412693.jpgRyeqdHfmkBXzD8JxCrqI5qqmbTQw5xjgErJHPle0s7I9wtoDSbAC9yujIpxowi7pHIdSTybMVPCGNDBoAHtufSsqItpAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgP/2Q==">')




    
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.



def home(request):
    return render(request,'lobby.html')

def auditorium(request):
    return render(request,'auditorium.html')

def selfie(request):
    return render(request, 'selfie.html')

def selfie2(request):
    return render(request, 'selfie2.html')

def selfie3(request):
    return render(request, 'selfie3.html')

def project(request):
    return render(request, 'project.html')

def archive(request):
    return render(request, 'archive.html')

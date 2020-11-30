from django.shortcuts import render, redirect
from django.http import HttpResponse
from mainproject.core.models import *
from django.core.files.storage import FileSystemStorage
import os

# Translating section

def index(request):

    return render(request,'index.html')

def portifolio_details(request):

    return render(request, 'portfolio-details.html')

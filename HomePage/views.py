from django.shortcuts import render
from django.http import HttpResponse 
from django.template.loader import render_to_string
# Create your views here.

def home(request):
    home=render_to_string("aboutme.html")
    return render(request,"headerfooter.html",{'content':home})
from django.shortcuts import render
from django.http import HttpResponse 
from django.template.loader import render_to_string
# Create your views here.

def home(request):
    home_var=render_to_string("aboutme.html")
    return render(request,"headerfooter.html",{'content':home_var})

def portfolio(request):
    portfolio_var=render_to_string("portfolio.html")
    return render(request,"headerfooter.html",{'content':portfolio_var})

def art(request):
    art_var=render_to_string("art.html")
    return render(request,"headerfooter.html",{'content':art_var})

def resume(request):
    resume_var=render_to_string("resume.html")
    return render(request,"headerfooter.html",{'content':resume_var})
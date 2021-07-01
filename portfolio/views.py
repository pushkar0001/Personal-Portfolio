from django.shortcuts import render
from . models import Project



# Create your views here.
def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'context':projects})

def contact(request):
    
    return render(request, 'nav-pages/contact.html' )

def servicess(request):
    return render(request, 'nav-pages/servicess.html' )
    
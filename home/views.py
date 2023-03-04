from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request) :
    # return HttpResponse("This is Homepage of my first Django project")
    context = { #Context is a set of variables which is sent to the HTML file
        'variable': 'This is sent',
        'name' : 'Pramit Kumar Kar'
    }
    
    return render(request,'index.html',context)
def about(request) :
    # return HttpResponse("This is About Page of my first Django project")
    return render(request,'about.html')
def services(request) :
    # return HttpResponse("This is Web Dev Services Page of my first Django project")
    return render(request,'services.html')
def contact(request) :
    # return HttpResponse("This is the Contact Page of my first Django project").
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, password=password, date=datetime.today())
        contact.save()
        messages.success(request, 'Your Details has been successfully stored.')
    return render(request,'contact.html')
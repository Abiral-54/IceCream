from django.shortcuts import render
from datetime import datetime
from home.models import contact
from django.contrib import messages
# Create your views here.
def index(request):
    context ={
        "variable1":"Abiral is learning django with in 1 year",
        "variable2":"Abiral will learn django with a great hope of outcome"
    }
    messages.success(request,"this is the text message")
    return render (request, 'index.html',context)
    #return HttpResponse("this is homepage")
def about(request):
    return render (request, 'about.html')
    
def services(request):
    return render (request, 'services.html')
    
def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact = contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent.")
    return render (request, 'contact.html')
    
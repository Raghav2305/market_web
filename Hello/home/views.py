from django.shortcuts import render, HttpResponse
from home.models import Contact
from datetime import datetime
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        desc = request.POST.get('issue')
        
        contact = Contact(email=email, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your query has been sent!')

    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

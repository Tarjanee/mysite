from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact

# Create your views here.
def index(request):
    context = {
        'variable1': "this is sent",
        'variable2': "this is sent"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("this is home page.")

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        try:
            contact = Contact(name=name, email=email, phone=phone, city=city, date=datetime.today())
            contact.save()
        except Exception as e:
            print(f"Error saving contact: {e}")

    return render(request, 'contact.html')

def dessert(request):
    return render(request, 'dessert.html')

def pizza(request):
    return render(request, 'pizza.html')

def drink(request):
    return render(request, 'drink.html')

def indian(request):
    return render(request, 'indian.html')

def indian_sweets(request):
    return render(request, 'indian_sweets.html')

def indian_chaat(request):
    return render(request, 'indian_chaat.html')

from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def coaching(request):
    return render(request, 'coaching.html')

def time(request):
    return render(request, 'time.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')


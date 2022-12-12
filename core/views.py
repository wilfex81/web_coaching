from django.shortcuts import render

def home(request):
    """Retruns the contents of the mainpage"""
    return render(request, 'index.html')

def about(request):
    """Returns the contents of the about page"""
    return render(request, 'about.html')

def coaching(request):
    ''''Returns the contents of the coaching page'''
    return render(request, 'coaching.html')

def time(request):
    '''Returns the contents of the time page
    Time page in this case is the time the lessons take place'''
    return render(request, 'time.html')

def contact(request):
    '''In this page we can contact the admin'''
    return render(request, 'contact.html')

def login(request):
    '''Login page'''
    return render(request, 'login.html')


from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home, name= 'home'),
    path('about/',views.about, name= 'about'),
    path('coaching/',views.coaching, name= 'coaching'),
    path('time/',views.time, name= 'time'),
    path('contact/',views.contact, name= 'contact'),
    path('login/',views.login, name= 'login'),
]
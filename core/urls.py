from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/',views.home, name= 'home'),
    path('about/',views.about, name= 'about'),
    path('coaching/',views.coaching, name= 'coaching'),
    path('time/',views.time, name= 'time'),
    path('contact/',views.contact, name= 'contact'),
    path('login/',views.login, name= 'login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
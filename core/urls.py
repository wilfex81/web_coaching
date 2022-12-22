from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/',views.home, name= 'home'),
    path('about/',views.about, name= 'about'),
    path('courses/',views.courses, name= 'courses'),
    path('detail/',views.detail, name= 'detail'),
    path('features/',views.features, name= 'features'),
    path('team/',views.team, name= 'team'),
    path('testimonial/',views.testimonial, name= 'testimonial'),
    path('contact/',views.contact, name= 'contact'),
    path('login/',views.login, name= 'login'),
    path('subscribe/', views.subscribe, name = 'subscribe'),
    path("newsletter/", views.newsletter, name= 'newsletter')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
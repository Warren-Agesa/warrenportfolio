from django.urls import path
from . import views

urlpatterns = [

        path('', views.index, name="index"),
        path('about/', views.about_view, name="about"),
        path('contact/', views.contact, name="contact"),
        path('resume/', views.resume, name="resume"),
        path('services/', views.services, name="services"),
        path('portfolio/', views.Portfolio, name="portfolio"),
]
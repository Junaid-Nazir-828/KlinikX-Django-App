from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),

    path('gallery/', views.gallery, name='gallery'),
    path('gallery/hair_transplant', views.gallery_hair_transplant, name='gallery_hair_transplant'),
    path('gallery/dental', views.gallery_dental, name='gallery_dental'),
    path('gallery/cosmetic', views.gallery_cosmetic, name='gallery_cosmetic'),
    path('gallery/eye_surgery', views.gallery_eye_surgery, name='gallery_eye_surgery'),
    path('gallery/ivf', views.gallery_ivf, name='gallery_ivf'),
    path('gallery/plastic', views.gallery_plastic, name='gallery_plastic'),


    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'), 
    path('t&c/', views.terms_and_conditions, name='terms_and_conditions'), 
    path('privacy/', views.privacy, name='privacy'), 
    path('services/', views.services, name='services'),
    path('hair_transplant/', views.hair_transplant, name='hair_transplant'),
    path('plastic/', views.plastic, name='plastic'),
    path('cosmetic/', views.cosmetic, name='cosmetic'),
    path('dental/', views.dental, name='dental'),
    path('art/', views.art, name='art'),
    path('eye_surgery/', views.eye_surgery, name='eye_surgery'),

    # path('chatbot/',views.chatbot, name='chatbot'),
]

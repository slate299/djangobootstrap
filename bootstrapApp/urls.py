from django.urls import path

from bootstrapApp import views

urlpatterns=[
    path('', views.index, name='index'),
    path('about.html/', views.about, name='about'),
    path('contact.html/', views.contact, name='contact'),
    path('shop.html/', views.shop, name='shop'),
    path('skating.html/', views.skating, name='skating'),

]
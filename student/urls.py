
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('start/<int:pk>',views.start,name='start'),
    path('done',views.done,name='done'),
    path('history',views.history,name='history')
    
]

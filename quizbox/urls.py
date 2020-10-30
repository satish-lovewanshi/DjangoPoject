from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('quizmake',views.QuizMake,name='QuizMake'),
    path('AddQues',views.AddQues,name='AddQues')
]

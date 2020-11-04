from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('quizmake',views.QuizMake,name='QuizMake'),
    path('AddQues/<int:pk>',views.AddQues,name='AddQues'),
    path('edit',views.edit,name='edit'),
    path('manage',views.manage,name='manage'),
    path('delete_test/<int:pk>',views.delete_test,name='delete_test'),
    path('edit_test/<int:pk>',views.edit_test,name='edit_test')

]

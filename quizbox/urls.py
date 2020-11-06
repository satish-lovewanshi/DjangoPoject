from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('quizmake',views.QuizMake,name='QuizMake'),
    path('AddQues/<int:pk>',views.AddQues,name='AddQues'),
    path('edit',views.edit,name='edit'),
    path('manage_test',views.manage_test,name='manage_test'),
    path('manage_ques/<int:pk>',views.manage_ques,name='manage_ques'),

    path('delete_test/<int:pk>',views.delete_test,name='delete_test'),
    path('delete_ques/<int:pk>',views.delete_ques,name='delete_ques'),

    path('edit_test/<int:pk>',views.edit_test,name='edit_test'),
    path('edit_ques/<int:pk>',views.edit_ques,name="edit_ques"),


]

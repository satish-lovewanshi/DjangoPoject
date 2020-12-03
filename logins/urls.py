from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('LoginPage',views.LoginPage,name='LoginPage'),
    path('StudentLogin',views.StudentLogin,name='StudentLogin'),
   
    # path('signup',views.signup,name='signup'),

    path('signup_as',views.signup_as,name='signup_as'),
    path('StudentSignUp',views.StudentSignUp,name='StudentSignUp'),
    path('TeacherSignUp',views.TeacherSignUp,name='TeacherSignUp'),
    path('UpdateProfile',views.UpdateProfile,name='UpdateProfile'),
    path('ranking',views.ranking,name='ranking'),

    path('LogoutUser',views.LogoutUser,name='LogoutUser'),
]

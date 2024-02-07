from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    # path('',views.home,name='home'),
    path('homeU.html',views.homeU,name='homeU.html'),
    path('homeL.html',views.homeL,name='homeL.html'),
    path('signup.html',views.signup,name='signup.html'),
    path('login.html',views.loginn,name='login.html'),
    path('editM.html',views.editM,name='editM.html'),
    path('homeU.html',views.signout,name='homeU.html'), 
    path('editU.html',views.editU,name='editU.html'),
    path('editD.html',views.editD,name='editD.html'),
    path('editP.html',views.editP,name='editP.html'),
]
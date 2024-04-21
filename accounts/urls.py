from django.contrib import admin
from django.urls import path,include
from django.urls.conf import include
from . import views

urlpatterns = [
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('statistics',views.statistics,name="statistics"),
    path("vaccine",views.vaccine,name="vaccine"),
    path("covid",views.covid,name="covid"),
    path("result",views.result,name="result"),
    
]


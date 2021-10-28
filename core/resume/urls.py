from django.urls import path
from .import views

urlpatterns = [
    
     path('', views.index),
     path('linkdin',views.linkdin,name='linkdin'),
]

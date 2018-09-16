from django.urls import path

from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.Home.as_view(), name='home'),
]
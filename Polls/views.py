from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse


class Home(TemplateView):
    template_name = 'home.html'
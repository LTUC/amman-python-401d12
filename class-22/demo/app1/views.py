from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    # process this req (home req)
    template_name = 'home.html'

class AboutPageView(TemplateView):
    # process this req (home req)
    template_name = 'about.html'
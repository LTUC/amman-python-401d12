from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView
from .models import Pet

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class PetsListView(ListView):
    model= Pet
    template_name = "pets_list.html"
    context_object_name = "pets_objs"

class PetDetailsView(DetailView):
    model = Pet
    template_name = "pet_details.html"
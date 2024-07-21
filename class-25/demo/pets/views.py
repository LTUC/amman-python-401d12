from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Pet
from django.urls import reverse_lazy

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

class PetCreateView(CreateView):
    model=Pet
    template_name = 'pet_create.html'
    fields = ['owner', 'name', 'des', 'breed']

class PetUpdateView(UpdateView):
    model = Pet
    template_name="pet_update.html"
    fields = "__all__"

class PetDeleteView(DeleteView):
    model=Pet
    template_name='pet_delete.html'
    success_url = reverse_lazy('pets')

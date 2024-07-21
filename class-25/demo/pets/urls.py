
from django.contrib import admin
from django.urls import path
from .views import HomePageView, PetsListView, PetDetailsView, PetCreateView, PetUpdateView, PetDeleteView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('pets', PetsListView.as_view(), name='pets'),
    path('<int:pk>', PetDetailsView.as_view(), name="pet_details"),
    path('create', PetCreateView.as_view(), name='create_pet'),
    path('update/<int:pk>', PetUpdateView.as_view(), name="pet_update"),
    path('delete/<int:pk>', PetDeleteView.as_view(), name="pet_delete")
]

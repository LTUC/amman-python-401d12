
from django.contrib import admin
from django.urls import path
from .views import HomePageView, PetsListView, PetDetailsView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('pets', PetsListView.as_view(), name='pets'),
    path('<int:pk>', PetDetailsView.as_view(), name="pet_details")
]

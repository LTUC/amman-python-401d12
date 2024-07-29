from django.urls import path
from .views import home_view, uni_details_view

urlpatterns = [
    path('', home_view, name='home'),
    path('<int:pk>', uni_details_view, name="details")
]

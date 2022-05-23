from django.urls import path
from locations.views import listLocations

urlpatterns = [
    path('', listLocations),
]

from django.urls import path
from doctors.views import listDoctors

urlpatterns = [
    path('', listDoctors),

]
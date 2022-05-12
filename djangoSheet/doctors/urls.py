from django.urls import path
from doctors.views import list_doctors, show, create_doctor


urlpatterns = [
    path('', list_doctors),
    path('<int:id>/', show),
    path('create/', create_doctor),
]

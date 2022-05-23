from django.urls import path
from user.views import listUsers

urlpatterns = [
    path('', listUsers),

]
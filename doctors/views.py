from django.http import HttpResponse
from django.shortcuts import render
from doctors.models import doctors

# Create your views here.
def listDoctors(request):
    qs = doctors.objects.all()
    context = {'doctors_list' : qs}
    return render(request, 'doctors/doctors_list.html', context)
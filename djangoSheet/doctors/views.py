from django.http import HttpResponse
from django.shortcuts import render
from doctors.models import Doctors
from doctors.forms import DoctorForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def list_doctors(request):
    qs = Doctors.objects.all()
    context = {'list_doctors' : qs}
    return render(request, 'doctors/list_doctors.html', context)

def show(request, id):
    doctor = Doctors.objects.get(id=id)
    return render (request, 'doctors/show.html', {'doctor': doctor})

def create_doctor(request):
    form = DoctorForm()
    return render(request, 'doctors/create.html', {'form': form})

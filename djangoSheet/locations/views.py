from django.shortcuts import render
from django.shortcuts import render
from locations.models import locations

# Create your views here.
def listLocations(request):
    qs = locations.objects.all()
    context = {'locations_list' : qs}
    return render(request, 'locations/locations_list.html', context)
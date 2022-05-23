from django.http import HttpResponse
from django.shortcuts import render
from user.models import user

# Create your views here.
def listUsers(request):
    qs = user.objects.all()
    context = {'user_list' : qs}
    return render(request, 'user/user_list.html', context)
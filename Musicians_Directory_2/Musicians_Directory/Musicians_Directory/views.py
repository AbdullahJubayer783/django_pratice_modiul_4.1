from django.shortcuts import render , redirect

from Album.models import Albums


def home(request):
    data = Albums.objects.all()
    print(data)
    return render(request, 'index.html',{'data':data})
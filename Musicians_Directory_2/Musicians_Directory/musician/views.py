from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.

def edit_details(request , id):
    post = models.Musicians.objects.get(pk = id)
    form = forms.MusicianForm(instance=post)
    if request.method == 'POST':
        form = forms.MusicianForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'musician.html',{'form' : form})
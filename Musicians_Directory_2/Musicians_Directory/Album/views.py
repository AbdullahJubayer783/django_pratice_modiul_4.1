from django.shortcuts import render , redirect
from . import forms
from . import models
# Create your views here.

def edit_post(request , id):
    post = models.Albums.objects.get(pk = id)
    print(post)
    form = forms.MusicianForm(instance=post)
    if request.method == 'POST':
        form = forms.MusicianForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'Album.html',{'form' : form})

def delete_post(request,id):
    post = models.Albums.objects.get(pk = id)
    post.delete()
    return redirect("home")
from django import forms
from .models import Albums

class MusicianForm(forms.ModelForm):
    class Meta:
        model = Albums
        fields = '__all__'
        widgets = {
            'Rating' : forms.RadioSelect
        }
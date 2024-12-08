from django import forms
from films.models import Film

class FilmCreate(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'
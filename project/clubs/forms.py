from django import forms

from .models import Club
class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ['introduction', 'cover']
        # fields = ['introduction', 'avatar', 'is_visable']
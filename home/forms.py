from django import forms
from .models import Search


class searchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = ['address',]
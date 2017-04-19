from django import forms
from .models import searchData

class searchForm(forms.Form):
    name = forms.CharField(label='Name:', max_length=128)
    addr = forms.CharField(label='Email Address:', max_length=128)
    term = forms.CharField(label='Search Terms:', max_length=1024)
    
    def process(self):
        cd = self.cleaned_data
        d = searchData(name=cd['name'],address=cd['addr'],terms=cd['term'])
        d.save()

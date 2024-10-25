from django import forms

class MovieForm(forms.Form):
    
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title'}), label='')
    year = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Year'}), label='')
    genre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'genre'}), label='')
    duration = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'duration'}), label='')
    language = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'language'}), label='')
    rating = forms.FloatField(widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'rating'}), label='')
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'rows':3, 'placeholder':'Description'}), label='')
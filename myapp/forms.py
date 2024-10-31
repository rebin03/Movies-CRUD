from django import forms
from myapp.models import Movie

class MovieForm(forms.Form):
    
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title'}), label='')
    year = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Year'}), label='')
    genre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'genre'}), label='')
    duration = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'duration'}), label='')
    language = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'language'}), label='')
    rating = forms.FloatField(widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'rating'}), label='')
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'rows':3, 'placeholder':'Description'}), label='')
    poster = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control'}), label='Movie Poster', label_suffix='')
    
    
class MovieUpdateForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title'}),
            'year':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Year'}),
            'genre':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Gemre'}),
            'duration':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Duration'}),
            'language':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Language'}),
            'rating':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Rating'}),
            'description':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description', 'rows':'5'}),
            'poster':forms.FileInput(attrs={'class':'form-control'})
        }
        
        labels = {
            'title':'',
            'year':'',
            'genre':'',
            'duration':'',
            'language':'',
            'rating':'',
            'description':'',
            'poster':'Choose movie poster'
        }
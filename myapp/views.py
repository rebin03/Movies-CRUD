from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from myapp.forms import MovieForm
from myapp.models import Movie

# Create your views here.

class MovieCreateView(View):
    
    template = 'movie_add.html'
    form_class = MovieForm
    
    def get(self, request, *args, **kwargs):
        
        
        form = self.form_class()
        
        return render(request, self.template, {'form':form, 'heading':'Add Movies', 'button':'ADD'})
    
    def post(self, request, *args, **kwargs):
        
        form_data = request.POST
        form = self.form_class(form_data)
        
        if form.is_valid():
            data = form.cleaned_data
            
            print(data)
            Movie.objects.create(**data)
            return redirect('movie-list')
            
        return render(request, self.template, {'form':form, 'heading':'Add Movies', 'button':'ADD'})
    
    
class MovieListView(View):
    
    template = 'movie_list.html'
    
    def get(self, request, *args, **kwargs):
        
        qs = Movie.objects.all()
        
        return render(request, self.template, {'data':qs})
    
    
class MovieDetailView(View):
    
    template = 'movie_detail.html'
    
    def get(self, request, *args, **kwargs):
        
        id = kwargs.get('pk')
        movie = Movie.objects.get(id=id)
        
        genre = movie.genre
        genre_list = genre.split(', ')
        
        return render(request, self.template, {'movie':movie, 'genre_list':genre_list})
    
    
class MovieDeleteView(View):
    
    def get(self, request, *args, **kwargs):
        
        id = kwargs.get('pk')
        Movie.objects.get(id=id).delete()
        
        return redirect('movie-list')
    

class MovieUpdateView(View):
    
    template = 'movie_add.html'
    form_class = MovieForm
    
    def get(self, request, *args, **kwargs):
        
        id = kwargs.get('pk')
        movie_obj = get_object_or_404(Movie, id=id)

        data = {
            'title':movie_obj.title,
            'year':movie_obj.year,
            'genre':movie_obj.genre,
            'duration':movie_obj.duration,
            'language':movie_obj.language,
            'rating':movie_obj.rating,
            'description':movie_obj.description,
        }

        form = self.form_class(initial=data)
        
        return render(request, self.template, {'form':form, 'heading':'Update Movie', 'button':'Update'})
    
    
    def post(self, request, *args, **kwargs):
        
        form_data = request.POST
        form = self.form_class(form_data)
        id = kwargs.get('pk')
        
        if form.is_valid():
            data = form.cleaned_data
            
            Movie.objects.filter(id=id).update(**data)
            return redirect('movie-list')
        
        return render(request, self.template, {'form':form, 'heading':'Update Movie', 'button':'Update'})
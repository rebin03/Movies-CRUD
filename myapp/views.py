from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from myapp.forms import MovieForm, MovieUpdateForm, SignUpForm, SignInForm
from myapp.models import Movie
from django.db.models import Q
from django.contrib.auth.models import User

# Create your views here.

class MovieCreateView(View):
    
    template = 'movie_add.html'
    form_class = MovieForm
    
    def get(self, request, *args, **kwargs):
        
        form = self.form_class()
        
        return render(request, self.template, {'form':form, 'heading':'Add Movies', 'button':'ADD'})
    
    def post(self, request, *args, **kwargs):
        
        form_data = request.POST
        files = request.FILES
        form = self.form_class(form_data, files)
        
        if form.is_valid():
            data = form.cleaned_data
            
            print(data)
            Movie.objects.create(**data)
            return redirect('movie-list')
            
        return render(request, self.template, {'form':form, 'heading':'Add Movies', 'button':'ADD'})
    
    
class MovieListView(View):
    
    template = 'movie_list.html'
    
    def get(self, request, *args, **kwargs):
        
        search_text = request.GET.get('filter')
        
        qs = Movie.objects.all()
        
        if search_text:
            qs = Movie.objects.filter(
                Q(title__contains=search_text)|
                Q(genre__contains=search_text)|
                Q(language__contains=search_text)
            )
            
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
    form_class = MovieUpdateForm
    
    def get(self, request, *args, **kwargs):
        
        id = kwargs.get('pk')
        movie_obj = get_object_or_404(Movie, id=id)

        form = self.form_class(instance=movie_obj)
        
        return render(request, self.template, {'form':form, 'heading':'Update Movie', 'button':'Update'})
    
    
    def post(self, request, *args, **kwargs):
        
        form_data = request.POST
        files = request.FILES
        
        id = kwargs.get('pk')
        movie_obj = get_object_or_404(Movie, id=id)
        
        form = self.form_class(form_data, files, instance=movie_obj)
        
        if form.is_valid():
            
            form.save()
            return redirect('movie-list')
        
        return render(request, self.template, {'form':form, 'heading':'Update Movie', 'button':'Update'})
    
    
class SignUpView(View):
    
    template_name = 'signup_signin.html'
    form_class = SignUpForm
    
    def get(self, request, *args, **kwargs):
        
        form = self.form_class()

        return render(request, self.template_name, {'form': form, 'heading':'Sign Up'})
    
    
    def post(self, request, *args, **kwargs):
        
        form_data = request.POST
        form = self.form_class(form_data)
        
        if form.is_valid():
            
            data = form.cleaned_data
            User.objects.create_user(**data)
            return redirect('signin')

        return render(request, self.template_name, {'form': form, 'heading': 'Sign Up'})
    

class SignInView(View):
    
    template_name = 'signup_signin.html'
    form_class = SignInForm
    
    def get(self, request, *args, **kwargs):
        
        form = self.form_class()
        
        return render(request, self.template_name, {'form': form, 'heading': 'Sign In'})
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from myapp.forms import MovieForm, MovieUpdateForm, SignUpForm, SignInForm
from myapp.models import Movie
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from myapp.decorators import signin_required
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.db.models import Q

# Create your views here.

decorators = [signin_required, never_cache]

@method_decorator(decorators, name='dispatch')
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
    
 
@method_decorator(decorators, name='dispatch')   
class MovieListView(View):
    
    template = 'movie_list.html'
    
    def get(self, request, *args, **kwargs):
        
        search_text = request.GET.get('filter')
        
        all__title = Movie.objects.values_list('title', flat=True).distinct()
        all__genre = Movie.objects.values_list('genre', flat=True).distinct()
        all__language = Movie.objects.values_list('language', flat=True).distinct()
        
        all_record = []
        all_record.extend(all__title)
        all_record.extend(all__genre)
        all_record.extend(all__language)
        
        qs = Movie.objects.all()
        
        if search_text:
            qs = Movie.objects.filter(
                Q(title__contains=search_text)|
                Q(genre__contains=search_text)|
                Q(language__contains=search_text)
            )
            
        return render(request, self.template, {'data':qs, 'records':all_record})
    

@method_decorator(decorators, name='dispatch')    
class MovieDetailView(View):
    
    template = 'movie_detail.html'
    
    def get(self, request, *args, **kwargs):
        
        id = kwargs.get('pk')
        movie = Movie.objects.get(id=id)
        
        genre = movie.genre
        genre_list = genre.split(', ')
        
        return render(request, self.template, {'movie':movie, 'genre_list':genre_list})
    

@method_decorator(decorators, name='dispatch')    
class MovieDeleteView(View):
    
    def get(self, request, *args, **kwargs):
        
        id = kwargs.get('pk')
        Movie.objects.get(id=id).delete()
        
        return redirect('movie-list')
    

@method_decorator(decorators, name='dispatch')
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
    
    
    def post(self, request, *args, **kwargs):
        
        form_data = request.POST
        form = self.form_class(form_data)

        if form.is_valid():
            
            data = form.cleaned_data
            
            # fetch user credential
            uname = data.get('username')
            pwd = data.get('password')

            # Check the credential is valid or not
            user_obj = authenticate(request, username=uname, password=pwd)

            # Create user session if the credential is valid
            if user_obj:
                
                 login(request, user_obj)
                 
                 return redirect('movie-list')
        
        return render(request, self.template_name, {'form': form, 'heading': 'Sign In'})
    

@method_decorator(decorators, name='dispatch')    
class SignOutView(View):
    
    def get(self, request, *args, **kwargs):
        
        logout(request)

        return redirect('signin')
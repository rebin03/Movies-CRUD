"""
URL configuration for movies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/list/', views.MovieListView.as_view(), name='movie-list'),
    path('movie/add/', views.MovieCreateView.as_view(), name='movie-add'),
    path('movie/detail/<int:pk>', views.MovieDetailView.as_view(), name='movie-detail'),
    path('movie/remove/<int:pk>', views.MovieDeleteView.as_view(), name='movie-delete'),
    path('movie/update/<int:pk>', views.MovieUpdateView.as_view(), name='movie-update'),
    path('register/', views.SignUpView.as_view(), name='register'),
    path('', views.SignInView.as_view(), name='signin'),
    path('signout/', views.SignOutView.as_view(), name='signout'),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
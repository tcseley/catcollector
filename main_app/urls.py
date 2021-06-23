from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about' ),
    path('index/', views.index, name='index')
]

# When thinking about making a webpage inside of django- first step would be:
# 1. create a view function
# 2. create your html page
# 3. Create a path inside of urls.py (maim_app)
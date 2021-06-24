from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about' ),
    path('index/', views.index, name='index'),
    path('cats/', views.cats_index, name='cat_index'),
    path('cats/<int:cat_id>/', views.cats_show, name='cats_show'),
    path('cats/create/', views.CatCreate.as_view(), name='cats_create'),
    path('cats/<int:pk>/update/', views.CatUpdate.as_view(), name='cats_update'),
    path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cats_delete'),
    path('user/<username>/', views.profile, name='profile'),
    path('cattoys/', views.cattoys_index, name='cattoys_index'),
    path('cattoys/<int:cattoy_id>', views.cattoys_show, name='cattoys_show'),
    path('cattoys/create/', views.CatToyCreate.as_view(), name='cattoys_create'),
    path('cattoys/<int:pk>/update/', views.CatToyUpdate.as_view(), name='cattoys_update'),
    path('cattoys/<int:pk>/delete/', views.CatToyDelete.as_view(), name='cattoys_delete'),
]

# When thinking about making a webpage inside of django- first step would be:
# 1. create a view function
# 2. create your html page
# 3. Create a path inside of url
from django.contrib import admin
from .models import Cat, CatToy

#Import models
from .models import Cat

# Register your models here.
admin.site.register(Cat)
admin.site.register(CatToy)


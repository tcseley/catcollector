from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'about.html')

def index(request):
    return render(request, 'index.html')

# Before we create our function, we are going to make a class

class Cat:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age
cats = [
    Cat('Lolo', 'tabby', 'foul little demon', 3),
    Cat('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
    Cat('Raven', 'black tripod', '3 legged cat', 4)
]

def cats_index(request):
    data ={
        'cats': cats
    }
    return render(request, 'cats/index.html', data)


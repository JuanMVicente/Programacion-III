from django.shortcuts import render

# Create your views here.
from .models import Film, Author, Genre, FilmInstance

def index(request):
    num_films = Film.objects.all().count()
    num_instance = FilmInstance.objects.all().count()
    num_authors = Author.objects.all().count()

    disponibles = FilmInstance.objects.filter(status__exact='a').count()

    return render(
        request,
        'index.html',
        context={
            'num_films': num_films,
            'num_authors': num_authors,
            'disponibles': disponibles,
            'num_instance': num_instance
        }
    )

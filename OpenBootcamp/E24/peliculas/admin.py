from django.contrib import admin

from .models import Author, Genre, Film, FilmInstance

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Film)
admin.site.register(FilmInstance)

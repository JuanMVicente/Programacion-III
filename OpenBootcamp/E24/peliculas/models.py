import uuid
from django.db import models
from django.urls import reverse

class Genre(models.Model):
    name = models.CharField(max_length=64, help_text="Nombre del género")

    def __str__(self):
        return self.name


class Film(models.Model):
    title = models.CharField(max_length=32)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=100, help_text="Descripción de la película")
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('film-detail',args=[str(self.id)])

class FilmInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único de la película")
    film = models.ForeignKey('Film', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.CharField(max_length=50, null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True,default='m', help_text='Estado de la pelicula')

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        return f'{self.id} ({self.film.title})'


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True,blank=True)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
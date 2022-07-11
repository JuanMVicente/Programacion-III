# Generated by Django 4.0.6 on 2022-07-10 21:54

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('summary', models.TextField(help_text='Descripción de la película', max_length=100)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='peliculas.author')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nombre del género', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='FilmInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='ID único de la película', primary_key=True, serialize=False)),
                ('imprint', models.CharField(max_length=200)),
                ('due_back', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(blank=True, choices=[('m', 'Maintenance'), ('o', 'On loan'), ('a', 'Available'), ('r', 'Reserved')], default='m', help_text='Estado de la pelicula', max_length=1)),
                ('film', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='peliculas.film')),
            ],
            options={
                'ordering': ['due_back'],
            },
        ),
        migrations.AddField(
            model_name='film',
            name='genre',
            field=models.ManyToManyField(to='peliculas.genre'),
        ),
    ]

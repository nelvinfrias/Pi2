from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)

class Post(models.Model):
    image = models.ImageField(upload_to='new_post')
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    link = models.URLField(max_length=200)
    texto = models.TextField()
    Category = [
        ('Educación básica', 'Educación básica'),
        ('Educación secundaria', 'Educación secundaria'),
        ('Bachillerato', 'Bachillerato'),
        ('Técnico', 'Técnico'),
        ('Profesional titulado', 'Profesional titulado'),
        ('Diplomado', 'Diplomado'),
        ('Maestría', 'Maestría'),
        ('Doctorado', 'Doctorado'),
      
    ]

    Category = models.CharField(
        max_length=20,
        choices=Category,
        default='Profesional'
    )
    


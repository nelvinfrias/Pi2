from django.db import models

class Post(models.Model):
    image = models.ImageField(upload_to='new_post')
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    link = models.URLField(max_length=200)
    texto = models.TextField()



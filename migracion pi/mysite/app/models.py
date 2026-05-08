from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Category(models.Model):
    name = models.CharField(max_length=200)


class Post(models.Model):
    image   = models.ImageField(upload_to='new_post')
    titulo  = models.CharField(max_length=200)
    autor   = models.CharField(max_length=200)
    link    = models.URLField(max_length=200)
    texto   = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL,
                                null=True, blank=True,
                                related_name='posts')  # ← línea nueva

    CATEGORIAS = [
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
        choices=CATEGORIAS,
        default='Profesional'
    )


class Profile(models.Model):
    user      = models.OneToOneField(User, on_delete=models.CASCADE,
                                     related_name='profile')
    foto      = models.ImageField(upload_to='perfiles/', blank=True, null=True)
    biografia = models.TextField(blank=True, default='')
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Perfil de {self.user.username}'

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'


@receiver(post_save, sender=User)
def crear_perfil(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def guardar_perfil(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()
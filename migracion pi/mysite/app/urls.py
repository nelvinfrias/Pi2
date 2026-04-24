from django.urls import path
from django.views.generic import RedirectView  # ← agrega este import
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='/login/'), name='index'),  # ← agrega esta línea
    path('home/', views.home, name='home'),
    path('post/', views.Post),
    path('generos/', views.Generos),
    path('barra/', views.barra),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('perfil/', views.perfil, name='perfil'),            # ← agrega
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
]
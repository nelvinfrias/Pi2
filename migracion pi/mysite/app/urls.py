from django.urls import path
from django.views.generic import RedirectView
from . import views
from django.urls import path, include

urlpatterns = [
    path('', RedirectView.as_view(url='/login/'), name='index'),
    path('home/', views.home, name='home'),
    path('post/', views.Post),
    path('generos/', views.Generos),
    path('barra/', views.barra),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('usuarios/', views.buscar_usuarios, name='buscar_usuarios'),          # ← agrega
    path('usuarios/<str:username>/', views.ver_perfil, name='ver_perfil'),     # ← agrega
    path('test/', views.test_view, name='test'),
    path('accounts/', include('allauth.urls')), 
    path('like/<int:id>/', views.like_post, name='like_post'),
    path('comentarios/<int:id>/', views.comentarios_post, name='comentarios_post'),
    path('libro/<int:pk>/', views.detalle_libro, name='detalle_libro'),
    path('libro/<int:pk>/resena/', views.resena_completa, name='resena_completa'),
]
from django.urls import path, include
from django.views.i18n import set_language
from . import views

urlpatterns = [
    path('i18n/setlang/', set_language, name='set_language'),

    path('', views.barra, name='barra'),
    path('home/', views.home, name='home'),
    path('post/', views.Post),
    path('generos/', views.Generos),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('usuarios/', views.buscar_usuarios, name='buscar_usuarios'),
    path('usuarios/<str:username>/', views.ver_perfil, name='ver_perfil'),
    path('accounts/', include('allauth.urls')),
    path('like/<int:id>/', views.like_post, name='like_post'),
    path('libro/<int:pk>/comentar/', views.comentarios_post, name='comentarios_post'),
    path('libro/<int:pk>/', views.detalle_libro, name='detalle_libro'),
    path('libro/<int:pk>/resena/', views.resena_completa, name='resena_completa'),
    path('libro-api/<str:clave>/', views.libro_api, name='libro_api'),
    path('eliminar-post/<int:id>/', views.eliminar_post, name='eliminar_post'),
    path('barradeinicio/', views.barradeinicio, name='barradeinicio'),
]
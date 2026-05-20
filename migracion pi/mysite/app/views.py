from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import NewPost as forms, SignUpForm, ProfileForm
from .models import Post as task, Profile
import requests
from cloudinary import CloudinaryImage



def home(request):

    # OPEN LIBRARY API
    url = "https://openlibrary.org/search.json?q=education"
    response = requests.get(url)
    if response.headers.get('Content-Type') == 'application/json':
        data = response.json()
    else:
        print("No llegó JSON")
        print(response.text)
        data = []

    libros = data.get("docs", [])[:15]

    # POSTS
    post = task.objects.all().order_by('-id')

    q = request.GET.get('q')
    categoria = request.GET.get('categoria')

    if q:
        post = post.filter(titulo__icontains=q)

    if categoria:
        post = post.filter(Category=categoria)

    contexto = {
        'i': post,
        'libros': libros
    }

    return render(request, "main.html", contexto)


def libro_api(request, clave):

    url = f"https://openlibrary.org/works/{clave}.json"

    response = requests.get(url)
    libro = response.json()

    autor = {"nombre": "Desconocido"}

    if "authors" in libro:
        autor_key = libro["authors"][0]["author"]["key"]
        autor_url = f"https://openlibrary.org{autor_key}.json"
        autor_response = requests.get(autor_url)
        autor = autor_response.json()

    contexto = {
        "libro": libro,
        "autor": autor
    }

    return render(request, "libro_api.html", contexto)


@login_required(login_url='/login/')
def Post(request):
    if request.method == "POST":
        i = forms(request.POST, request.FILES)
        if i.is_valid():
            post = i.save(commit=False)
            post.usuario = request.user
            post.save()
            return redirect("home")
        else:
            return render(request, "Newpost.html", {'i': i})
    else:
        return render(request, "Newpost.html", {'i': forms()})


def Generos(request):
    i = task.objects.all()
    return render(request, "generos.html", {'tag': i})


def barra(request):
    return render(request, "barradeinicio.html")


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error = 'Usuario o contraseña incorrectos.'
    return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='/login/')
def perfil(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    posts = task.objects.filter(usuario=request.user).order_by('-id')  # ← agrega
    return render(request, 'perfil.html', {'profile': profile, 'posts': posts})


@login_required(login_url='/login/')
def editar_perfil(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'editar_perfil.html', {'form': form})



def buscar_usuarios(request):
    query = request.GET.get('q', '')
    usuarios = []
    if query:
        usuarios = User.objects.filter(
            username__icontains=query
        ).exclude(id=request.user.id)
    return render(request, 'buscar_usuarios.html', {
        'usuarios': usuarios,
        'query': query
    })



def ver_perfil(request, username):
    usuario = get_object_or_404(User, username=username)
    profile, created = Profile.objects.get_or_create(user=usuario)
    posts = task.objects.filter(usuario=usuario).order_by('-id')  # ← agrega
    return render(request, 'ver_perfil.html', {
        'profile': profile,
        'usuario': usuario,
        'posts': posts  # ← agrega
    })
def detalle_libro(request, pk):
    libro = get_object_or_404(task, pk=pk)
    return render(request, "detalle_libro.html", {'libro': libro})
@login_required(login_url='/login/')
def resena_completa(request, pk):
    libro = get_object_or_404(task, pk=pk)
    return render(request, "resena_completa.html", {'libro': libro})


@login_required(login_url='/login/')
def like_post(request, id):
    post = get_object_or_404(task, id=id)

    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect('home')

@login_required(login_url='/login/')
def comentarios_post(request, id):
    post = get_object_or_404(task, id=id)
    return render(request, 'comentarios.html', {'post': post})

def test_view(request):
    return render(request, 'test.html')


@login_required(login_url='/login/')
def eliminar_post(request, id):
    post = get_object_or_404(task, id=id, usuario=request.user)

    if request.method == "POST":
        post.delete()
        return redirect('perfil')

    return redirect('perfil')
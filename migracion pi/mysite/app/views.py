from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import NewPost as forms, SignUpForm, ProfileForm
from .models import Post as task, Profile


@login_required(login_url='/login/')
def home(request):
    post = task.objects.all().order_by('-id')
    q = request.GET.get('q')
    categoria = request.GET.get('categoria')
    if q:
        post = post.filter(titulo__icontains=q)
    if categoria:
        post = post.filter(Category=categoria)
    return render(request, "main.html", {'i': post})


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


@login_required(login_url='/login/')
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


@login_required(login_url='/login/')
def ver_perfil(request, username):
    usuario = get_object_or_404(User, username=username)
    profile, created = Profile.objects.get_or_create(user=usuario)
    posts = task.objects.filter(usuario=usuario).order_by('-id')  # ← agrega
    return render(request, 'ver_perfil.html', {
        'profile': profile,
        'usuario': usuario,
        'posts': posts  # ← agrega
    })

def test_view(request):
    return render(request, 'test.html')



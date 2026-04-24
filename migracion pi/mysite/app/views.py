from django.shortcuts import render, redirect
from .forms import NewPost as forms
from .models import Post as task, Category
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import SignUpForm  
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SignUpForm

from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm
@login_required(login_url='/login/')
def home(request):
    post = task.objects.all()

    
    q = request.GET.get('q')
    categoria = request.GET.get('categoria')


    if q:
        post = post.filter(titulo__icontains=q)


    if categoria:
        post = post.filter(Category=categoria)

    return render(request, "main.html", {'i': post})


def Post(request):
    if request.method == "POST":
        i = forms(request.POST, request.FILES)
        if i.is_valid():
            i.save()
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


# ─── AGREGAR ESTOS IMPORTS AL INICIO DEL ARCHIVO ─────────────
 # ajusta el import si ya importas de forms


# ─── VISTA DE REGISTRO ────────────────────────────────────────
def signup(request):
    if request.user.is_authenticated:
        return redirect('/')   # si ya está logueado, redirige al inicio

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Iniciar sesión automáticamente tras el registro
            login(request, user)
            return redirect('/')  # cambia por tu URL principal
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})





# ── LOGIN ──────────────────────────────────────────────────────
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # si ya está logueado, va directo a home

    error = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # ← login exitoso → home
        else:
            error = 'Usuario o contraseña incorrectos.'

    return render(request, 'login.html', {'error': error})


# ── LOGOUT ─────────────────────────────────────────────────────
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='/login/')
def perfil(request):
    profile = request.user.profile
    return render(request, 'perfil.html', {'profile': profile})


@login_required(login_url='/login/')
def editar_perfil(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'editar_perfil.html', {'form': form})


# ── PROTEGER HOME con login_required ───────────────────────────


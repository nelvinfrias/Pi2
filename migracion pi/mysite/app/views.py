from django.shortcuts import render, redirect
from .forms import NewPost as forms
from .models import Post as task, Category

def home(request):
    post = task.objects.all()

    # 🔍 obtener filtros
    q = request.GET.get('q')
    categoria = request.GET.get('categoria')

    # filtro por texto (titulo)
    if q:
        post = post.filter(titulo__icontains=q)

    # filtro por categoría
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
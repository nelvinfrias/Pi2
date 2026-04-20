from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NewPost as forms
from .models import Post as task

def home(request):
    post = task.objects.all()
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
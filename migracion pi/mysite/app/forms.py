from django import forms

from .models import Post


class NewPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'titulo', 'autor', 'link', 'texto', 'Category']
        labels = {
            'image': '',
            'titulo': '',
            'autor': '',
            'link': '',
            'texto': '',
            'Category': '',
        }
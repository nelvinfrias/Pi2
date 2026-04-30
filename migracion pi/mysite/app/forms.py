from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Profile


class NewPost(forms.ModelForm):

    class Meta:
        model = Post

        fields = [
            'image',
            'titulo',
            'autor',
            'link',
            'texto',
            'Category'
        ]

        labels = {
            'image': '',
            'titulo': '',
            'autor': '',
            'link': '',
            'texto': '',
            'Category': '',
        }


class SignUpForm(UserCreationForm):

    email = forms.EmailField(
        required=True,
        label='Correo electrónico',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'tu@email.com'
        })
    )

    class Meta:

        model = User

        fields = (
            'username',
            'email',
            'password1',
            'password2'
        )

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de usuario'
            }),
        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['password2'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['username'].label = 'Usuario'
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].label = 'Confirmar contraseña'

    def clean_email(self):

        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Este correo electrónico ya está registrado.'
            )

        return email

    def clean_username(self):

        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                'Este nombre de usuario ya está en uso.'
            )

        return username


class ProfileForm(forms.ModelForm):

    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre de usuario'
        })
    )

    class Meta:

        model = Profile

        fields = (
            'username',
            'foto',
            'biografia'
        )

        widgets = {

            'biografia': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Cuéntanos algo sobre ti...'
            }),

        }

        labels = {
            'username': 'Nombre de usuario',
            'foto': 'Foto de perfil',
            'biografia': 'Biografía',
        }

    def __init__(self, *args, **kwargs):

        user = kwargs.pop('user', None)

        super().__init__(*args, **kwargs)

        if user:
            self.fields['username'].initial = user.username

    def save(self, commit=True):

        profile = super().save(commit=False)

        profile.user.username = self.cleaned_data['username']
        profile.user.save()

        if commit:
            profile.save()

        return profile
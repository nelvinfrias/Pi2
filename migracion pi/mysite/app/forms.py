from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Post
from .models import Profile


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

# ─── AGREGAR ESTOS IMPORTS AL INICIO DEL ARCHIVO ─────────────
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


# ─── FORMULARIO DE REGISTRO ───────────────────────────────────
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
        model  = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de usuario'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Agregar clases CSS a los campos de contraseña
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
        # Personalizar labels
        self.fields['username'].label = 'Usuario'
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].label = 'Confirmar contraseña'

    # ── Validación: email único ──
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Este correo electrónico ya está registrado.'
            )
        return email

    # ── Validación: username único (UserCreationForm ya lo hace,
    #    pero lo explicitamos con mensaje en español) ──
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                'Este nombre de usuario ya está en uso.'
            )
        return username
    from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('foto', 'biografia')
        widgets = {
            'biografia': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Cuéntanos algo sobre ti...'
            }),
        }
        labels = {
            'foto': 'Foto de perfil',
            'biografia': 'Biografía',
        }
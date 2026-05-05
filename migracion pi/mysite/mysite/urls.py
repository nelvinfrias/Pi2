from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from allauth.account.views import PasswordResetFromKeyView
from django.shortcuts import redirect


class CustomPasswordResetFromKeyView(PasswordResetFromKeyView):
    def form_valid(self, form):
        form.save()  # guarda la nueva contraseña
        return redirect('account_login')


urlpatterns = [
    path('admin/', admin.site.urls),

    
    path('', include('app.urls')),
                                                    # ← tus rutas existentes
    path(
        'accounts/password/reset/key/<uidb36>-<key>/', 
        CustomPasswordResetFromKeyView.as_view(), 
        name='account_reset_password_from_key'),

    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
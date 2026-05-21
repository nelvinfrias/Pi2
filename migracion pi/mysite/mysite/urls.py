from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from allauth.account.views import PasswordResetFromKeyView
from django.shortcuts import redirect


class CustomPasswordResetFromKeyView(PasswordResetFromKeyView):
    def form_valid(self, form):
        form.save()
        return redirect('/login/?reset=ok')



urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]


urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),

    path('', include('app.urls')),

    path(
        'accounts/password/reset/key/<uidb36>-<key>/',
        CustomPasswordResetFromKeyView.as_view(),
        name='account_reset_password_from_key'
    ),

    path('accounts/', include('allauth.urls')),
)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
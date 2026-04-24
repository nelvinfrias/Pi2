from django.contrib import admin
from .models import Category, Post
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Profile

admin.site.register(Post)
admin.site.register(Category)




# ─── Inline para ver el Profile dentro del User ───────────────
class ProfileInline(admin.StackedInline):
    model  = Profile
    can_delete = False
    verbose_name_plural = 'Perfil'
    fields = ('foto', 'biografia')


# ─── Extiende el UserAdmin con el inline ──────────────────────
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)


# ─── Re-registrar User con el nuevo admin ─────────────────────
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


# ─── Registrar Profile por separado también ───────────────────
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display  = ('user', 'creado_en')
    search_fields = ('user__username', 'user__email')
    readonly_fields = ('creado_en',)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Especialidad, Equipo, Campo

class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ('email', 'username', 'nombre', 'apellido', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Información Personal', {'fields': ('nombre', 'apellido', 'especialidades', 'equipos')}),
        ('Permisos', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'nombre', 'apellido', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email', 'username', 'nombre', 'apellido')
    ordering = ('email',)

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Especialidad)
admin.site.register(Equipo)
admin.site.register(Campo)

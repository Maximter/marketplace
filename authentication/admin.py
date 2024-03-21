from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

# Создание форм для создания и изменения пользователей
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'first_name', 'last_name',)

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'birthday', 'is_active', 'is_staff', 'activated', 'deleted')

class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = ['email', 'first_name', 'last_name', 'is_staff', 'is_active', 'activated']
    list_filter = ['is_staff', 'is_active', 'activated']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'birthday')}),
        (_('Permissions'), {'fields': ('is_staff', 'is_active', 'activated', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'created_date')}),
        (_('Status'), {'fields': ('deleted',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'birthday', 'password1', 'password2', 'is_staff', 'is_active', 'activated'),
        }),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
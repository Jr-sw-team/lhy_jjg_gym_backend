from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _

from .forms import UserCreationForm, UserChangeForm
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('get_full_name', 'email', 'username', 'is_superuser', 'is_trainer')
    list_display_links = ('get_full_name',)
    list_filter = ('is_superuser',)

    def get_fieldsets(self, request, obj=None):
        add_fieldsets = (
            (_('Initial info'), {'fields': ('email', 'password1', 'password2')}),
            (_('Personal info'), {'fields': ('username', 'phone_number')}),
            (_('Permissions'), {'fields': ('is_superuser',)}),
            (_('Is trainer'), {'fields': ('is_trainer',)}),
            (_('Profile picture'), {'fields': ('profile_pic',)}),
            (_('Career'), {'fields': ('career',)}),
        )
        return add_fieldsets

    search_fields = ('email', 'username')
    ordering = ('-pk',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)

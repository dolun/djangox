from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Garde

# class CustomUserChangeForm(UserChangeForm):
#     class Meta(UserChangeForm.Meta):
#         model = CustomUser

# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ['email', 'username','first_name','last_name','estAccepte']


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    list_display = ("username", "email", "points", "estAccepte", "is_staff")
    fieldsets = ((None, {'fields': ('estAccepte',
                                    'first_name2','last_name2',
                                    'adresse',
                                    'telephone_fixe', 'telephone_portable',
                                    'enfant1',# 'naissance1',
                                    'enfant2',# 'naissance2',
                                    'enfant3',# 'naissance3',
                                    'enfant4',# 'naissance4',
                                    'points',
                                    )}),)+UserAdmin.fieldsets


class GardeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Garde._meta.get_fields()]
    # ('aGarde','debutGarde','finGarde','pointsATransferer','valide')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Garde, GardeAdmin)

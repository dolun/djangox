from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser,Garde


class GardeForm(forms.ModelForm):
    class Meta:
        model = Garde
        fields = ('aGarde', 'pointsATransferer',)


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email',
         'username',
         'first_name',
         'last_name',
         'first_name2',
         'last_name2',
         'adresse',
         )

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'username','first_name','last_name')
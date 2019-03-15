from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Garde
from bootstrap_datepicker_plus import DateTimePickerInput


# class GardeForm(forms.ModelForm):

#     class Meta:
#         model = Holiday
#         widgets = {
#             'holiday_date': forms.DateInput(attrs={'class':'datepicker'}),
#         }

class GardeForm(forms.ModelForm):
    class Meta:
        model = Garde
        # fields = ('aGarde',
        #           'debutGarde',
        #           'finGarde',
        #           'pointsATransferer',)
        exclude = ['aGarde', 'valide', 'pub_date']


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username',
                  'email',
                  'first_name', 'last_name',
                  'first_name2', 'last_name2',
                  'adresse',
                  'telephone_fixe', 'telephone_portable',
                  'enfant1',# 'naissance1',
                  'enfant2',# 'naissance2',
                  'enfant3',# 'naissance3',
                  'enfant4',# 'naissance4',
                  )

class CustomUserChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = CustomUser
        fields = ('email',
                  'first_name', 'last_name',
                  'first_name2', 'last_name2',
                  'adresse',
                  'telephone_fixe', 'telephone_portable',
                  'enfant1',# 'naissance1',
                  'enfant2',# 'naissance2',
                  'enfant3',# 'naissance3',
                  'enfant4',# 'naissance4',
                  )

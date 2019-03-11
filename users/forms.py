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
        exclude = ['aFaitGarder','valide','pub_date']


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
        fields = ('email', 'username', 'first_name', 'last_name')

from django.urls import path
from django.views.generic import ListView
from .views import InscriptionUserView,inscriptionUserView,annuaireView
from .models import CustomUser

urlpatterns = [
    # path('inscription/', InscriptionUserView.as_view(), name='account_inscription'),
    path('inscription/', inscriptionUserView, name='account_inscription'),
    # path('annuaire/', annuaireView,name='annuaire')    
    path('annuaire/',
        ListView.as_view(model=CustomUser,context_object_name="familles",template_name="pages/annuaire.html"),
        name='annuaire',),
]

from django.urls import path
from django.views.generic import ListView, TemplateView
from .views import InscriptionUserView, inscriptionUserView, annuaireView, declarationGardeView, DeclarationGardeCreate
from .models import CustomUser, Garde

urlpatterns = [
    # path('inscription/', InscriptionUserView.as_view(), name='account_inscription'),
    path('inscription/', inscriptionUserView, name='account_inscription'),
    # path('annuaire/', annuaireView,name='annuaire')

    # path('declaration-garde',declarationGardeView,name='declaration_garde'),
    path('declaration-garde', DeclarationGardeCreate.as_view(),
         name='declaration_garde'),

    path('annuaire/', ListView.as_view(model=CustomUser, context_object_name="familles", template_name="pages/annuaire.html"),
         name='annuaire',),
    path('commission', TemplateView.as_view(
        template_name="pages/commission.html"), name='commission'),
    path('garde_enregistree',TemplateView.as_view(
        template_name="pages/garde_enregistree.html"), name='garde_enregistree'),
]

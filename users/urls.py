from django.urls import path

from .views import InscriptionUserView,inscriptionUserView

urlpatterns = [
    # path('inscription/', InscriptionUserView.as_view(), name='account_inscription'),
    path('inscription/', inscriptionUserView, name='account_inscription'),
]

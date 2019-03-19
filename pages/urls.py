from django.urls import path

from .views import HomePageView, AboutPageView, homePageView, gardeValidee,gardesView,familleView,AnnoncesView
from .models import Annonce
from django.views.generic import ListView
from users.models import Garde

urlpatterns = [
    # path('', HomePageView.as_view(), name='home'),
    path('', homePageView, name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('annonces/',
         ListView.as_view(
             queryset = Annonce.objects.order_by('-date'),
             context_object_name="annonces",
             template_name="pages/annonces.html"),
        #  AnnoncesView.as_view(),
         name='annonces',),
    path('garde_validee/', gardeValidee, name='garde_validee'),
    path('gardes/', gardesView,name='gardes'),
    path('famille/<id_famille>', familleView, name="famille")
]

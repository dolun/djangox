from django.urls import path

from .views import HomePageView, AboutPageView, homePageView, gardeValidee
from .models import Annonce
from django.views.generic import ListView

urlpatterns = [
    # path('', HomePageView.as_view(), name='home'),
    path('', homePageView, name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('annonces/',
         ListView.as_view(
             model=Annonce,
             context_object_name="annonces",
             template_name="pages/annonces.html"),
         name='annonces',),
    path('garde_validee/', gardeValidee, name='garde_validee'),
]

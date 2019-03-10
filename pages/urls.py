from django.urls import path

from .views import HomePageView, AboutPageView
from .models import Annonce
from django.views.generic import ListView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('annonces/',
         ListView.as_view
         (model=Annonce,
          context_object_name="annonces",
          template_name="pages/annonces.html"),
         name='annonces',),
]

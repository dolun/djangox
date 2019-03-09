from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from .forms import CustomUserCreationForm

class InscriptionUserView(TemplateView):
    template_name = 'pages/inscription.html'

def inscriptionUserView(request):
    form = CustomUserCreationForm(request.POST or None)

    if form.is_valid(): 
        # Ici nous pouvons traiter les données du formulaire
        # sujet = form.cleaned_data['sujet']
        # message = form.cleaned_data['message']
        # envoyeur = form.cleaned_data['envoyeur']
        # renvoi = form.cleaned_data['renvoi']
        # Nous pourrions ici envoyer l'e-mail grâce aux données 
        candidat = form.save(commit=False)
        # post.author = request.user
        # candidat.published_date = timezone.now()
        candidat.save()
        print("candidat enregistré",request.user.username)
        # que nous venons de récupérer

        envoi = True

    return render(request, 'pages/inscription.html', locals())
from django.shortcuts import render, redirect
# from django.core.urlresolvers import reverse_lazy
from django.urls import reverse
from django.utils import timezone

# Create your views here.
from django.views.generic import TemplateView, CreateView
from .forms import CustomUserCreationForm, GardeForm
from .models import CustomUser, Garde
from bootstrap_datepicker_plus import DateTimePickerInput
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import ModelChoiceField

# from .models import Choice, Question


class DeclarationGardeCreate(generic.edit.CreateView):
    model = Garde
    # model.pkFamille=self.request.user.pk
    # fields = ['aGarde',
    #           'debutGarde',
    #           'finGarde',
    #           'pointsATransferer']
    form_class = GardeForm
    template_name = "pages/declaration_garde.html"
    # success_url=reverse_lazy()
    #   context_object_name="garde"

    def form_valid(self, form):
        garde = form.save(commit=False)
        garde.aFaitGarder = self.request.user.username
        garde.pub_date = timezone.now()
        garde.save()
        print(f"garde enregistrée {garde.debutGarde} {garde.finGarde} ")
        # HttpResponseRedirect(obj.get_absolute_url())
        return redirect('garde_enregistree')

    def get_form(self):
        username = self.request.user.username
        print("get_form", username)
        form = super().get_form()
        form.fields['debutGarde'].widget = DateTimePickerInput(options={
            "format": 'DD/MM/YYYY HH:mm',
            "locale": "fr", }

        )
        form.fields['finGarde'].widget = DateTimePickerInput(options={
            "format": 'DD/MM/YYYY HH:mm',
            "locale": "fr", }
        )
        form.fields['aGarde'] = ModelChoiceField(queryset=CustomUser.objects.exclude(username=username),
                                                 label='Qui a gardé vos enfants?')
        return form

    def save(self):
        print("save garde")


def declarationGardeView(request):
    form = GardeForm(request.POST or None)
    if form.is_valid():
        pass
    return render(request, 'pages/declaration_garde.html', locals())


def annuaireView(request):
    return render(request, 'pages/annuaire.html', locals())


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
        print("candidat enregistré", request.user.username)
        # que nous venons de récupérer

        envoi = True

    return render(request, 'pages/inscription.html', locals())

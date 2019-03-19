from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from users.models import Garde, CustomUser
from users.forms import CustomUserChangeForm
from django.views.generic import ListView
from .models import Annonce

    # customUser=CustomUser.objects.get(username=request.user.username)
    # form = CustomUserChangeForm(request.POST or None,instance=customUser)


def familleView(request, id_famille):
    user = get_object_or_404(CustomUser, pk=id_famille)
    famille = CustomUserChangeForm(instance=user)
    for field in famille.fields:
        famille.fields[field].widget.attrs['readonly'] = True
    return render(request, 'pages/famille.html', {'famille': famille, 'nom': user.username})


def gardesView(request):
    gardesEffectuees = Garde.objects.filter(
        aGarde=request.user.username).order_by('-finGarde')
    gardesDemandees = Garde.objects.filter(
        aFaitGarder=request.user).order_by('-finGarde')
    return render(request, 'pages/gardes.html', locals())


def gardeValidee(request):
    user = request.user
    if not request.user.is_anonymous:
        gardesAValider = Garde.objects.filter(
            aFaitGarder=user).filter(valide=False)
        nbGardesAValider = gardesAValider.count()
        if nbGardesAValider > 0:
            garde = gardesAValider[0]
            gardien = CustomUser.objects.get(username=garde.aGarde)

            points = garde.pointsATransferer
            gardien.points += points
            user.points -= points
            garde.valide = True
            print(
                f"nb de points de la garde validee: {points}  ", user, gardien)
            garde.save()
            user.save()
            gardien.save()
            return render(request, 'pages/garde_validee.html')
    return TemplateView.as_view('pages/home.html')


def homePageView(request):
    user = request.user
    if not request.user.is_anonymous:
        print("XXXX", user)
        gardesAValider = Garde.objects.filter(
            aFaitGarder=user).filter(valide=False)
        print('gardesAValider', gardesAValider)
        nbGardesAValider = gardesAValider.count()
        print('nbGardesAValider', nbGardesAValider)
        if nbGardesAValider > 0:
            garde = gardesAValider[0]
            gardien = CustomUser.objects.get(username=garde.aGarde)
    return render(request, 'pages/home.html', locals())


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


class AnnoncesView(ListView):

    queryset = Annonce.objects.order_by('-date')
    context_object_name = "annonces"
    template_name = "pages/annonces.html"
    print(queryset)
    for annonce in queryset:
        print(annonce.photo)

from django.views.generic import TemplateView
from django.shortcuts import render
from users.models import Garde,CustomUser 


def gardesView(request):
    gardesEffectuees=Garde.objects.filter(aGarde=request.user).order_by('-finGarde')
    gardesDemandees=Garde.objects.filter(aFaitGarder=request.user.username).order_by('-finGarde')
    return render(request, 'pages/gardes.html', locals()) 

def gardeValidee(request):
    user=request.user
    if not request.user.is_anonymous:
        gardesAValider=Garde.objects.filter(aGarde=user).filter(valide=False)
        nbGardesAValider=gardesAValider.count()   
        if nbGardesAValider>0:
            garde=gardesAValider[0] 
            garde.aFaitGarder
            chezQui=CustomUser.objects.get(username=garde.aFaitGarder)

            points=garde.pointsATransferer
            chezQui.points-=points
            user.points+=points
            garde.valide=True
            print(f"nb de points de la garde validee: {points}  ",user,chezQui)
            garde.save()
            user.save()
            chezQui.save()
            return render(request, 'pages/garde_validee.html') 
    return  TemplateView.as_view('pages/home.html')

def homePageView(request):
    user=request.user
    if not request.user.is_anonymous:
        print("XXXX",user)
        gardesAValider=Garde.objects.filter(aGarde=user).filter(valide=False)
        print('gardesAValider',gardesAValider)
        nbGardesAValider=gardesAValider.count()  
        print('nbGardesAValider',nbGardesAValider) 
        if nbGardesAValider>0:
            garde=gardesAValider[0] 
            garde.aFaitGarder
            chezQui=CustomUser.objects.get(username=garde.aFaitGarder)
    return render(request, 'pages/home.html', locals()) 

class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class CustomUser(AbstractUser):
    pass
    estAccepte=models.BooleanField(default=False,verbose_name=" Famille acceptée")
    points=models.IntegerField(default=0,verbose_name="Points")
    first_name2=models.CharField(default='',max_length=100,
            verbose_name="prénom du second parent",blank=True)
    last_name2=models.CharField(default='',max_length=100,
        verbose_name="Nom du second parent",blank=True)
    adresse = models.CharField(max_length=200,verbose_name="Adresse de la famille" ,default='91120 Palaiseau')
    # telephone = models.
    def __str__(self):
        return self.username

class Garde(models.Model):
    # aFaitGarder=models.PositiveIntegerField(verbose_name='pk Famille',default=888)#models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    aFaitGarder=models.CharField(max_length=200, verbose_name='A fait garder',default="XXX")#models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    aGarde=models.ForeignKey(CustomUser,on_delete=models.CASCADE,verbose_name='Qui a gardé vos enfants?')
    debutGarde=models.DateTimeField(default=timezone.now,verbose_name='Heure de début de la garde')
    finGarde=models.DateTimeField(default=timezone.now,verbose_name='Heure de fin de la garde')
    pointsATransferer=models.PositiveIntegerField(verbose_name='Nombre de points de la garde',default=0)
    valide=models.BooleanField(default=False) 
    pub_date=models.DateTimeField(default=timezone.now,verbose_name='Date de déclaration')

    def __str__(self):
        return "garde "+str(self.pk)

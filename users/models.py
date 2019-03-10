from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass
    estAccepte=models.BooleanField(default=False,verbose_name=" Famille acceptée")
    points=models.IntegerField(default=0,verbose_name="Points")
    first_name2=models.CharField(default='',max_length=100,
            verbose_name="prénom du second parent",blank=True)
    last_name2=models.CharField(default='',max_length=100,
        verbose_name="Nom du second parent",blank=True)
    adresse = models.CharField(max_length=200,verbose_name="Adresse de la famille" )
    # telephone = models.
    def __str__(self):
        return self.username

class Garde(models.Model):
    pkFamille=models.PositiveIntegerField(verbose_name='pk Famille')#models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    aGarde=models.ForeignKey(CustomUser,on_delete=models.CASCADE,verbose_name='Qui a gardé les enfants?')
    pointsATransferer=models.PositiveIntegerField(verbose_name='Nombre de points de la garde')
    valide=models.BooleanField(default=False)
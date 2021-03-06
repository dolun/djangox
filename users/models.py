from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=32,
            verbose_name="prénom de la mère")
    last_name = models.CharField(max_length=32,
            verbose_name="nom de la mère")
    estAccepte=models.BooleanField(default=False,verbose_name=" Famille validée")
    points=models.IntegerField(default=0,verbose_name="Points")
    first_name2=models.CharField(default='',max_length=100,
            verbose_name="prénom du père",blank=True)
    last_name2=models.CharField(default='',max_length=100,
        verbose_name="Nom du père",blank=True)
    adresse = models.CharField(max_length=200,verbose_name="Adresse de la famille" ,default='91120 Palaiseau')

    telephone_fixe = models.CharField(default='01xxxxxxxx',verbose_name="Tél. fixe",max_length=10)
    telephone_portable = models.CharField(default='06xxxxxxxx',verbose_name="Tél. mobile",max_length=10)
    enfant1=models.CharField(blank=False,verbose_name="prénom et date de naissance enfant 1",max_length=150)
    enfant2=models.CharField(blank=True,verbose_name="prénom et date de naissance enfant 2",max_length=150)
    enfant3=models.CharField(blank=True,verbose_name="prénom et date de naissance enfant 3",max_length=150)
    enfant4=models.CharField(blank=True,verbose_name="prénom et date de naissance enfant 4",max_length=150)
    # telephone_fixe = RegexValidator(regex=r'^\+?1?\d{10}$', message="Téléphone fixe")
    # telephone_portable = RegexValidator(regex=r'^\+?1?\d{10}$', message="Téléphone fixe")
    # telephone = models.
    def __str__(self):
        return self.username

class Garde(models.Model):
    # aFaitGarder=models.PositiveIntegerField(verbose_name='pk Famille',default=888)#models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    aGarde=models.CharField(max_length=200, verbose_name='A gardé',default="XXX")#models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    aFaitGarder=models.ForeignKey(CustomUser,on_delete=models.CASCADE,verbose_name='Bénéficiaire de la garde?')
    debutGarde=models.DateTimeField(default=timezone.now,verbose_name='Heure de début de la garde')
    finGarde=models.DateTimeField(default=timezone.now,verbose_name='Heure de fin de la garde')
    pointsATransferer=models.PositiveIntegerField(verbose_name='Nombre de points de la garde',default=0)
    valide=models.BooleanField(default=False) 
    pub_date=models.DateTimeField(default=timezone.now,verbose_name='Date de déclaration')

    def __str__(self):
        return "garde "+str(self.pk)

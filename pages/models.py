from django.db import models
# from django.contrib.auth.models import User
from django.utils import timezone

class Annonce(models.Model):
    titre=models.CharField(verbose_name='Titre',blank=False,max_length=250)
    date=models.DateTimeField(verbose_name="Date de publication",default=timezone.now)
    contenu=models.TextField(blank=True)
    photo=models.FileField(blank=True,upload_to="photos/")
    def __str__(self):
        return self.titre

# class Profil(models.Model):

#     user = models.OneToOneField(User)  # La liaison OneToOne vers le modèle User
#     site_web = models.URLField(blank=True)
    # avatar = models.ImageField(null=True, blank=True, upload_to="avatars/")
    # signature = models.TextField(blank=True)
    # inscrit_newsletter = models.BooleanField(default=False)
    # accepte = models.BooleanField(default=False)

    # def __str__(self):
    #     return "Profil de {0}".format(self.user.username)


from django.contrib import admin
from django.utils.text import Truncator

# Register your models here.
from .models import Annonce

class AnnonceAdmin(admin.ModelAdmin):
    list_display = ('titre','date','apercu_contenu','photo')
    ordering       = ('date', )
    search_fields  = ('titre', 'contenu')
    list_filter    = ('titre','contenu')
    def apercu_contenu(self, annonce):
        """ 
        Retourne les 40 premiers caractères du contenu de l'article, 
        suivi de points de suspension si le texte est plus long. 
        On pourrait le coder nous même, mais Django fournit déjà la 
        fonction qui le fait pour nous !
        """
        return Truncator(annonce.contenu).chars(60, truncate='...')
    apercu_contenu.short_description = 'Aperçu du contenu'

admin.site.register(Annonce,AnnonceAdmin)
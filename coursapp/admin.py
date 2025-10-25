from django.contrib import admin
from .models import Enseignant, Etudiant, Cours, Seance, Presence, CahierDeTexte

@admin.register(Enseignant)
class EnseignantAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom', 'email')
    search_fields = ('nom', 'prenom', 'email')

@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom', 'email', 'statut')
    search_fields = ('nom', 'prenom', 'email')
    list_filter = ('statut',)

@admin.register(Cours)
class CoursAdmin(admin.ModelAdmin):
    list_display = ('titre', 'enseignant')
    search_fields = ('titre',)
    list_filter = ('enseignant',)

@admin.register(Seance)
class SeanceAdmin(admin.ModelAdmin):
    list_display = ('cours', 'date')
    list_filter = ('date', 'cours')

@admin.register(Presence)
class PresenceAdmin(admin.ModelAdmin):
    list_display = ('seance', 'etudiant', 'present')
    list_filter = ('present',)

@admin.register(CahierDeTexte)
class CahierDeTexteAdmin(admin.ModelAdmin):
    list_display = ('seance',)

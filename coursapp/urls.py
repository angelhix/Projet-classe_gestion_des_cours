from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('cours/', views.liste_cours, name='liste_cours'),
    path('cours/creer/', views.creer_cours, name='creer_cours'),
    path('etudiants/', views.liste_etudiants, name='liste_etudiants'),
    path('etudiants/creer/', views.creer_etudiant, name='creer_etudiant'),
    path('etudiants/modifier/<int:pk>/', views.modifier_etudiant, name='modifier_etudiant'),
    path('etudiants/supprimer/<int:pk>/', views.supprimer_etudiant, name='supprimer_etudiant'),
    path('cours/<int:cours_id>/seances/', views.liste_seances, name='liste_seances'),
    path('cours/<int:cours_id>/seances/creer/', views.creer_seance, name='creer_seance'),
    path('seances/<int:seance_id>/presence/', views.prise_presence, name='prise_presence'),
    path('seances/<int:seance_id>/cahier-texte/', views.modifier_cahier_texte, name='modifier_cahier_texte'),

]

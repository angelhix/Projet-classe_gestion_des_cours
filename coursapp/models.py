from django.db import models
from django.contrib.auth.models import User

class Enseignant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    statut = models.CharField(max_length=20, choices=[('actif', 'Actif'), ('inactif', 'Inactif')], default='actif')

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Cours(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE, related_name='cours')

    def __str__(self):
        return self.titre

class Seance(models.Model):
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE, related_name='seances')
    date = models.DateField()
    contenu = models.TextField(blank=True, null=True)  # 🆕 champ cahier de texte

    def __str__(self):
        return f"{self.cours.titre} - {self.date}"

class Presence(models.Model):
    seance = models.ForeignKey(Seance, on_delete=models.CASCADE, related_name='presences')
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    present = models.BooleanField(default=False)

    class Meta:
        unique_together = ('seance', 'etudiant')

    def __str__(self):
        return f"{self.etudiant} - {self.seance} - {'Présent' if self.present else 'Absent'}"

class CahierDeTexte(models.Model):
    seance = models.OneToOneField(Seance, on_delete=models.CASCADE, related_name='cahier_de_texte')
    contenu = models.TextField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Cahier de texte de {self.seance}"

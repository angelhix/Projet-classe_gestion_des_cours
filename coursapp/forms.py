from django import forms
from django.contrib.auth.models import User
from .models import Cours, Etudiant, Enseignant, Seance

class CoursForm(forms.ModelForm):
    class Meta:
        model = Cours
        fields = ['titre', 'description']  # Removed 'enseignant' since it's auto-assigned
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['nom', 'prenom', 'email', 'statut']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'statut': forms.Select(attrs={'class': 'form-control'}),
        }

class SeanceForm(forms.ModelForm):
    class Meta:
        model = Seance
        fields = ['date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

class CahierTexteForm(forms.ModelForm):
    class Meta:
        model = Seance
        fields = ['contenu']
        widgets = {
            'contenu': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
        }

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    role = forms.ChoiceField(choices=[('enseignant', 'Enseignant'), ('etudiant', 'Étudiant')], widget=forms.Select(attrs={'class': 'form-control'}))
    nom = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    prenom = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Les mots de passe ne correspondent pas.")
        return cleaned_data

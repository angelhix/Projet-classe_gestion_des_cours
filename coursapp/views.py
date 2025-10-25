from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Cours, Enseignant, Etudiant
from .forms import CoursForm, EtudiantForm, RegistrationForm
def liste_cours(request):
    cours = Cours.objects.all()
    return render(request, 'coursapp/liste_cours.html', {'cours': cours})

@login_required
def creer_cours(request):
    if request.method == 'POST':
        form = CoursForm(request.POST)
        if form.is_valid():
            cours = form.save(commit=False)
            try:
                enseignant = Enseignant.objects.get(user=request.user)
                cours.enseignant = enseignant
                cours.save()
                return redirect('liste_cours')
            except Enseignant.DoesNotExist:
                messages.error(request, "Vous n'êtes pas enregistré en tant qu'enseignant.")
                return redirect('liste_cours')
    else:
        form = CoursForm()
    return render(request, 'coursapp/creer_cours.html', {'form': form})


def liste_etudiants(request):
    etudiants = Etudiant.objects.all()
    return render(request, 'coursapp/liste_etudiants.html', {'etudiants': etudiants})

def creer_etudiant(request):
    if request.method == 'POST':
        form = EtudiantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_etudiants')
    else:
        form = EtudiantForm()
    return render(request, 'coursapp/creer_etudiant.html', {'form': form})

def modifier_etudiant(request, pk):
    etudiant = get_object_or_404(Etudiant, pk=pk)
    if request.method == 'POST':
        form = EtudiantForm(request.POST, instance=etudiant)
        if form.is_valid():
            form.save()
            return redirect('liste_etudiants')
    else:
        form = EtudiantForm(instance=etudiant)
    return render(request, 'coursapp/modifier_etudiant.html', {'form': form})

def supprimer_etudiant(request, pk):
    etudiant = get_object_or_404(Etudiant, pk=pk)
    if request.method == 'POST':
        etudiant.delete()
        return redirect('liste_etudiants')
    return render(request, 'coursapp/supprimer_etudiant.html', {'etudiant': etudiant})
from django.shortcuts import redirect

def accueil(request):
    if request.user.is_authenticated:
        return redirect('liste_cours')
    else:
        return redirect('login')

from .models import Seance, Cours, Etudiant, Presence
from .forms import SeanceForm
from django.forms import modelformset_factory


def liste_seances(request, cours_id):
    cours = get_object_or_404(Cours, id=cours_id)
    seances = cours.seances.all().order_by('-date')
    return render(request, 'coursapp/liste_seances.html', {'cours': cours, 'seances': seances})

@login_required
def creer_seance(request, cours_id):
    cours = get_object_or_404(Cours, id=cours_id)
    # Check if user is the teacher of this course
    try:
        enseignant = Enseignant.objects.get(user=request.user)
        if cours.enseignant != enseignant:
            messages.error(request, "Vous n'avez pas l'autorisation de gérer ce cours.")
            return redirect('liste_cours')
    except Enseignant.DoesNotExist:
        messages.error(request, "Vous n'êtes pas enregistré en tant qu'enseignant.")
        return redirect('liste_cours')

    if request.method == 'POST':
        form = SeanceForm(request.POST)
        if form.is_valid():
            seance = form.save(commit=False)
            seance.cours = cours
            seance.save()
            return redirect('liste_seances', cours_id=cours.id)
    else:
        form = SeanceForm()
    return render(request, 'coursapp/creer_seance.html', {'form': form, 'cours': cours})
from django.forms import modelformset_factory

@login_required
def prise_presence(request, seance_id):
    seance = get_object_or_404(Seance, id=seance_id)
    # Check if user is the teacher of this course
    try:
        enseignant = Enseignant.objects.get(user=request.user)
        if seance.cours.enseignant != enseignant:
            messages.error(request, "Vous n'avez pas l'autorisation de gérer ce cours.")
            return redirect('liste_cours')
    except Enseignant.DoesNotExist:
        messages.error(request, "Vous n'êtes pas enregistré en tant qu'enseignant.")
        return redirect('liste_cours')

    etudiants = Etudiant.objects.filter(statut='actif').order_by('nom')

    PresenceFormSet = modelformset_factory(Presence, fields=('present',), extra=0)

    # On initialise ou récupère les présences existantes pour cette séance et ces étudiants
    presences = []
    for etu in etudiants:
        presence_obj, created = Presence.objects.get_or_create(seance=seance, etudiant=etu)
        presences.append(presence_obj)

    if request.method == 'POST':
        formset = PresenceFormSet(request.POST, queryset=Presence.objects.filter(seance=seance))
        if formset.is_valid():
            formset.save()
            return redirect('liste_seances', cours_id=seance.cours.id)
    else:
        formset = PresenceFormSet(queryset=Presence.objects.filter(seance=seance))

    # On envoie aussi les étudiants pour l’affichage
    etudiant_forms = zip(etudiants, formset.forms)

    return render(request, 'coursapp/prise_presence.html', {
        'seance': seance,
        'formset': formset,
        'etudiant_forms': etudiant_forms,
    })
from .forms import CahierTexteForm

@login_required
def modifier_cahier_texte(request, seance_id):
    seance = get_object_or_404(Seance, id=seance_id)
    # Check if user is the teacher of this course
    try:
        enseignant = Enseignant.objects.get(user=request.user)
        if seance.cours.enseignant != enseignant:
            messages.error(request, "Vous n'avez pas l'autorisation de gérer ce cours.")
            return redirect('liste_cours')
    except Enseignant.DoesNotExist:
        messages.error(request, "Vous n'êtes pas enregistré en tant qu'enseignant.")
        return redirect('liste_cours')

    if request.method == 'POST':
        form = CahierTexteForm(request.POST, instance=seance)
        if form.is_valid():
            form.save()
            return redirect('liste_seances', cours_id=seance.cours.id)
    else:
        form = CahierTexteForm(instance=seance)
    return render(request, 'coursapp/modifier_cahier_texte.html', {
        'seance': seance,
        'form': form
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('liste_cours')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    return render(request, 'coursapp/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            role = form.cleaned_data['role']
            nom = form.cleaned_data['nom']
            prenom = form.cleaned_data['prenom']

            # Créer l'utilisateur
            user = User.objects.create_user(username=username, password=password, email=email)

            if role == 'enseignant':
                Enseignant.objects.create(user=user, nom=nom, prenom=prenom, email=email)
            elif role == 'etudiant':
                Etudiant.objects.create(nom=nom, prenom=prenom, email=email)

            # Connecter l'utilisateur après inscription
            login(request, user)
            return redirect('liste_cours')
    else:
        form = RegistrationForm()
    return render(request, 'coursapp/register.html', {'form': form})

# 📚 Système de Gestion des Cours

Un **système web complet de gestion des cours** développé avec Django, conçu pour faciliter l'administration des enseignements et le suivi des étudiants. Cette application web permet aux enseignants et aux étudiants de gérer leurs cours, présences et contenus pédagogiques de manière efficace et centralisée.

---

## ✨ Fonctionnalités Principales

### 🔐 **Authentification & Autorisation**
- **Inscription dynamique** : Support pour deux rôles d'utilisateurs (Enseignant/Étudiant)
- **Connexion sécurisée** : Système de login/logout avec authentification Django
- **Contrôle d'accès** : Vérification des permissions pour chaque opération sensible
- **Profils distincts** : Interfaces adaptées selon le rôle de l'utilisateur

### 📖 **Gestion des Cours**
- **Création et consultation** : Les enseignants peuvent créer et gérer leurs cours
- **Listes dynamiques** : Affichage des cours avec description détaillée
- **Association enseignant** : Chaque cours est lié à un enseignant responsable
- **Hiérarchie organisée** : Structure claire entre cours → séances → présences

### 👥 **Gestion des Étudiants**
- **Répertoire centralisé** : Liste complète de tous les étudiants
- **CRUD complet** : Créer, consulter, modifier et supprimer des étudiants
- **Statuts flexibles** : Distinction entre étudiants actifs et inactifs
- **Données personnelles** : Stockage sécurisé du nom, prénom et email

### 📅 **Gestion des Séances**
- **Planification des cours** : Créer des séances avec dates spécifiques
- **Cahier de texte** : Ajouter du contenu pédagogique pour chaque séance
- **Historique complet** : Consultation des séances passées et futures
- **Tri chronologique** : Affichage organisé par date

### ✅ **Prise de Présence**
- **Feuille de présence** : Interface de gestion des présences par séance
- **Gestion en masse** : Marquer rapidement les étudiants présents/absents
- **Persistence** : Sauvegarde automatique des présences
- **Formset Django** : Gestion élégante de multiples enregistrements

### 📝 **Cahier de Texte**
- **Contenu pédagogique** : Documenter le contenu de chaque séance
- **Notes et observations** : Champ de notes pour annotations supplémentaires
- **Lien direct** : Association automatique avec la séance correspondante
- **Édition flexible** : Modifier le cahier après la séance

---

## 🏗️ Architecture du Projet

### Structure Générale
```
Projet-classe_gestion_des_cours/
├── gestion_cours/              # Configuration Django principal
│   ├── settings.py             # Paramètres de l'application
│   ├── urls.py                 # Routage principal
│   ├── wsgi.py                 # Déploiement WSGI
│   └── asgi.py                 # Support ASGI
├── coursapp/                   # Application principale
│   ├── models.py               # Modèles de données
│   ├── views.py                # Vues et logique métier
│   ├── forms.py                # Formulaires
│   ├── urls.py                 # Routage spécifique
│   ├── admin.py                # Configuration admin Django
│   ├── templates/              # Templates HTML
│   └── migrations/             # Migrations de base de données
├── db.sqlite3                  # Base de données SQLite
├── manage.py                   # Script de gestion Django
└── requirements.txt            # Dépendances Python
```

### Modèles de Données

#### **User (Django Auth)**
- Modèle standard Django pour l'authentification

#### **Enseignant**
```python
- user: OneToOneField(User)         # Lien avec l'utilisateur
- nom: CharField(100)               # Nom de famille
- prenom: CharField(100)            # Prénom
- email: EmailField(unique=True)    # Email professionnel
```

#### **Étudiant**
```python
- nom: CharField(100)               # Nom de famille
- prenom: CharField(100)            # Prénom
- email: EmailField(unique=True)    # Email personnel
- statut: CharField(20)             # 'actif' ou 'inactif'
```

#### **Cours**
```python
- titre: CharField(200)             # Nom du cours
- description: TextField()          # Détail du contenu
- enseignant: ForeignKey(Enseignant)  # Responsable du cours
```

#### **Séance**
```python
- cours: ForeignKey(Cours)          # Cours parent
- date: DateField()                 # Date de la séance
- contenu: TextField()              # Cahier de texte intégré
```

#### **Présence**
```python
- seance: ForeignKey(Seance)        # Séance concernée
- etudiant: ForeignKey(Étudiant)    # Étudiant
- present: BooleanField()           # Marqueur présence
- unique_together: (seance, etudiant)  # Une entrée par étudiant/séance
```

#### **CahierDeTexte**
```python
- seance: OneToOneField(Seance)     # Séance associée
- contenu: TextField()              # Contenu pédagogique
- notes: TextField()                # Annotations additionnelles
```

---

## 🛠️ Technologies Utilisées

| Technologie | Version | Utilisation |
|-------------|---------|-------------|
| **Django** | 5.2.6 | Framework web principal |
| **Python** | 3.x | Langage backend |
| **SQLite** | - | Base de données |
| **HTML/CSS** | - | Templates frontend (50.4%) |
| **Bootstrap/CSS** | - | Styling responsive |
| **xhtml2pdf** | 0.2.17 | Export PDF (potentiel) |
| **Pillow** | 11.3.0 | Traitement d'images |
| **reportlab** | 4.4.4 | Génération de rapports |

### Dépendances Complètes
Django, mysqlclient, Pillow, reportlab, xhtml2pdf, pyHanko, pypdf, requests, et autres utilitaires de support.

---

## 🚀 Installation & Configuration

### Prérequis
- Python 3.8+
- pip (gestionnaire de paquets Python)
- Environnement virtuel (recommandé)

### Étapes d'Installation

1. **Cloner le repository**
   ```bash
   git clone https://github.com/angelhix/Projet-classe_gestion_des_cours.git
   cd Projet-classe_gestion_des_cours
   ```

2. **Créer et activer un environnement virtuel**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Windows: venv\Scripts\activate
   ```

3. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

4. **Appliquer les migrations**
   ```bash
   python manage.py migrate
   ```

5. **Créer un superutilisateur**
   ```bash
   python manage.py createsuperuser
   ```

6. **Lancer le serveur de développement**
   ```bash
   python manage.py runserver
   ```

   L'application est accessible à : `http://localhost:8000/`

7. **Accéder à l'interface administrateur**
   ```
   http://localhost:8000/admin/
   ```

---

## 📋 Cas d'Usage Typiques

### Pour un **Enseignant** :
1. ✍️ **S'inscrire** sur la plateforme avec le rôle "Enseignant"
2. 📚 **Créer des cours** et ajouter des descriptions
3. 📅 **Créer des séances** pour organiser les enseignements
4. ✅ **Gérer les présences** à chaque séance
5. 📝 **Remplir le cahier de texte** avec le contenu enseigné
6. 📊 **Suivre les absences** des étudiants

### Pour un **Étudiant** :
1. 📝 **S'inscrire** sur la plateforme avec le rôle "Étudiant"
2. 👁️ **Consulter** la liste des cours disponibles
3. 📅 **Voir les séances** et leurs contenus
4. 🔍 **Accéder au cahier de texte** pour reviser

---

## 🔄 Flux de Travail Applicationnel

```
Login/Register
     ↓
Dashboard (Redirects to cours list)
     ↓
    ├─→ Enseignant: Manage own courses
    │    ├─→ Créer Cours
    │    ├─→ Créer Séances
    │    ├─→ Gérer Présences
    │    └─→ Remplir Cahier de Texte
    │
    └─→ Étudiant: View courses & content
         ├─→ Consulter Cours
         ├─→ Voir Séances
         └─→ Lire Cahier de Texte
```

---

## 🔒 Sécurité & Contrôle d'Accès

- **Décorateur `@login_required`** : Protection des vues critiques
- **Vérification d'autorisation** : Chaque enseignant gère uniquement ses cours
- **Isolation des données** : Les étudiants n'accèdent qu'aux cours existants
- **Mot de passe sécurisé** : Validation de confirmation lors de l'inscription

---

## 📊 Statut du Projet

✅ **Fonctionnalités complétées** (voir TODO.md):
- [x] Système d'inscription pour enseignants/étudiants
- [x] Gestion des cours
- [x] Gestion des étudiants (CRUD)
- [x] Gestion des séances et présences
- [x] Cahier de texte digital

---

## 🤝 Contribution

Les contributions sont bienvenues ! Pour contribuer :

1. **Fork** le repository
2. **Créer une branche** feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** vos changements (`git commit -m 'Add some AmazingFeature'`)
4. **Push** vers la branche (`git push origin feature/AmazingFeature`)
5. **Ouvrir une Pull Request**

---

## 📄 Licence

Ce projet est fourni tel quel pour usage éducatif et académique.

---

## 📞 Support & Contact

Pour toute question ou bug report, veuillez ouvrir une **Issue** sur GitHub.

**Développeur** : [angelhix](https://github.com/angelhix)

---

## 🎓 Utilisation Académique

Ce projet est idéal pour :
- 📚 **Établissements scolaires** : Gestion simplifiée des cours
- 🏫 **Centres de formation** : Suivi des sessions et présences
- 👨‍💻 **Apprentissage Django** : Exemple complet d'application web
- 📖 **Projets étudiants** : Référence pour architecture MVC

---

**Dernière mise à jour** : Octobre 2025  
**Version** : 1.0

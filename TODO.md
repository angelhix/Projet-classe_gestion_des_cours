# Tâches pour ajouter une page d'inscription pour enseignants ou étudiants

- [x] Ajouter RegistrationForm dans forms.py avec champs : username, password, confirm_password, email, role (enseignant/étudiant), nom, prénom
- [x] Ajouter register_view dans views.py : gérer la soumission du formulaire, créer User, puis Enseignant ou Etudiant selon le rôle, connecter l'utilisateur après inscription
- [x] Ajouter le chemin URL 'register/' dans urls.py pointant vers register_view
- [x] Créer le template register.html étendant base.html, avec le formulaire d'inscription
- [x] Mettre à jour login.html pour ajouter un lien vers la page d'inscription
- [x] Tester en lançant le serveur Django et vérifier l'inscription pour les deux rôles

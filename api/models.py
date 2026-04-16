from django.db import models
from django.contrib.auth.models import User

class Auteur(models.Model):
    nom = models.CharField(max_length=200)
    biographie = models.TextField(blank=True, null=True)
    nationalite = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nom


class Livre(models.Model):
    CATEGORIES = [
        ('roman', 'Roman'),
        ('science', 'Science'),
        ('histoire', 'Histoire'),
    ]

    titre = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)
    annee_publication = models.IntegerField()
    categorie = models.CharField(max_length=20, choices=CATEGORIES)
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE, related_name='livres')
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.titre


class Emprunt(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)
    date_emprunt = models.DateField(auto_now_add=True)
    date_retour = models.DateField()
    rendu = models.BooleanField(default=False)
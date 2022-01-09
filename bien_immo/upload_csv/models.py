from django.db import models
from django.contrib import admin

# Create your models here.

class lot(models.Model):
    id = models.CharField(max_length=150, primary_key=True)
    id_lot = models.CharField(max_length=150)
    nb_piece = models.IntegerField()
    typologie = models.CharField(max_length=50)
    prix_tva_reduit = models.FloatField()
    prix_tva_normal = models.FloatField()
    prix_ht = models.FloatField()
    prix_m_ht = models.FloatField()
    prix_m_ttc = models.FloatField()
    orientation = models.CharField(max_length=255)
    prix_tva_normal = models.FloatField()
    exterieur = models.BooleanField()
    balcony = models.BooleanField()
    garden = models.BooleanField()
    parking = models.IntegerField()
    ville = models.CharField(max_length=255)
    departement = models.IntegerField()
    date_fin_programme = models.CharField(max_length=255)
    adresse_entiere = models.CharField(max_length=255)
    date_extraction = models.DateField()

    def __str__(self):
        return self.name
import logging
from django.db import models
import datetime

logger = logging.getLogger(__name__)

class Categorie(models.Model):
    Productnaam = models.CharField(max_length=50)

    def __str__(self):
        return self.Productnaam

logger.debug('Categorie model geladen.')

class Klant(models.Model):
    Voornaam = models.CharField(max_length=50)
    Achternaam = models.CharField(max_length=50)
    Bedrijf = models.CharField(max_length=50)
    Facturatieadres = models.CharField(max_length=50)
    Adres = models.CharField(max_length=50)
    Telefoonnummer = models.CharField(max_length=18)
    Email = models.EmailField(max_length=100)
    Wachtwoord = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.Voornaam} {self.Achternaam}'

logger.debug('Klant model geladen.')

class Product(models.Model):
    Naam = models.CharField(max_length=100)
    EAN = models.CharField(max_length=50)
    Omschrijving = models.CharField(max_length=250, default='', blank=True, null=True)
    Prijs = models.DecimalField(default=0, decimal_places=0, max_digits=8)
    Categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='uploads/product/')
    Korting = models.BooleanField(default=False)
    Korting_prijs = models.DecimalField(default=0, decimal_places=0, max_digits=6)

    def __str__(self):
        return self.Naam

logger.debug('Product model geladen.')

class Bestelling(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Klant = models.ForeignKey(Klant, on_delete=models.CASCADE)
    Hoeveelheid = models.IntegerField(default=1)
    Adres = models.CharField(max_length=50)
    Telefoonnummer = models.CharField(max_length=18)
    Datum = models.DateField(default=datetime.datetime.today)
    Status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.Product)

logger.debug('Bestelling model geladen.')

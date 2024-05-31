from django.db import models
import datetime

#classes van mogelijke functies die gebruikt gaan worden op de website

#Categorieën van producten
class Categorie(models.Model):
    Productnaam = models.CharField(max_length=50)

    def __str__(self):
        return self.Productnaam
    
    class Meta:
        verbose_name_plural = 'Categorie'
    
#Klanten bestand
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
    
#Producten bestand
class Product(models.Model):

    Naam = models.CharField(max_length=100) #product.naam
    EAN = models.CharField(max_length=50) #product.EAN
    Omschrijving = models.CharField(max_length=250, default='', blank=True, null=True) #product.omschrijving
    Prijs = models.DecimalField(default=0, decimal_places=0, max_digits=8) #product.prijs
    Categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, default=1) #product.categorie
    Image = models.ImageField(upload_to='uploads/product/') #product.foto's
    #Kortingen/Blackfriday/Solden
    Korting = models.BooleanField(default=False)
    Korting_prijs = models.DecimalField(default=0, decimal_places=0, max_digits=6)

    def __str__(self):
        return self.Naam
    
#Bestellingen bestand
class Bestelling(models.Model):

    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Klant = models.ForeignKey(Klant, on_delete=models.CASCADE)
    Hoeveelheid = models.IntegerField(default=1)
    Adres = models.CharField(max_length=50)
    Telefoonnummer = models.CharField(max_length=18)
    Datum = models.DateField(default=datetime.datetime.today)
    Status = models.BooleanField(default=False)
      
    def __str__(self):
        return self.Product
    
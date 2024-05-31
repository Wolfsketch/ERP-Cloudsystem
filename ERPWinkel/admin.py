from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Categorie, Klant, Product, Bestelling

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('Productnaam',)
    search_fields = ('Productnaam',)

@admin.register(Klant)
class KlantAdmin(admin.ModelAdmin):
    list_display = ('Voornaam', 'Achternaam', 'Bedrijf', 'Email', 'Telefoonnummer')
    search_fields = ('Voornaam', 'Achternaam', 'Email', 'Bedrijf')
    list_filter = ('Bedrijf',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('Naam', 'EAN', 'Categorie', 'Prijs', 'Korting', 'Korting_prijs')
    search_fields = ('Naam', 'EAN', 'Categorie__Productnaam')
    list_filter = ('Categorie', 'Korting')
    readonly_fields = ('Image_preview',)
    fieldsets = (
        (None, {
            'fields': ('Naam', 'EAN', 'Omschrijving', 'Prijs', 'Categorie', 'Image', 'Image_preview')
        }),
        ('Kortingen', {
            'fields': ('Korting', 'Korting_prijs')
        }),
    )

    def Image_preview(self, obj):
        return mark_safe(f'<img src="{obj.Image.url}" width="200" height="200" />') if obj.Image else ""
    Image_preview.short_description = 'Image Preview'

@admin.register(Bestelling)
class BestellingAdmin(admin.ModelAdmin):
    list_display = ('Product', 'Klant', 'Hoeveelheid', 'Adres', 'Telefoonnummer', 'Datum', 'Status')
    search_fields = ('Product__Naam', 'Klant__Voornaam', 'Klant__Achternaam', 'Adres')
    list_filter = ('Status', 'Datum')
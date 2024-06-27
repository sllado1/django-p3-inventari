from django.db import models

# Create your models here.
class Categoria (models.Model):
    nom = models.CharField(max_length=100)
    descripcio = models.CharField(max_length=200)
    def __str__(self):
        return f'{self.nom}'
   
class Producte (models.Model):
    nom = models.CharField(max_length=100)
    descripcio = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.nom} - {self.categoria.nom}'

class Ubicacio(models.Model):
    nom = models.CharField(max_length=100)
    descripcio= models.CharField(max_length=200)
    def __str__(self):
        return f'{self.nom}'
    
class Exemplar (models.Model):
    ESTAT_PRODUCTE = (
        ('be', 'BÉ'),
        ('regular', 'REGULAR'),
        ('dolent', 'DOLENT'),
    )
    producte = models.ForeignKey(Producte, on_delete=models.CASCADE)
    estat = models.CharField(max_length=10, choices=ESTAT_PRODUCTE)
    num_serie = models.CharField(max_length=30)
    def __str__(self):
        return f'{self.producte.nom} - {self.num_serie} - {self.estat}'


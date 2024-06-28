from django.core.management.base import BaseCommand, CommandError
from random import randint

from faker import Faker
 
from inventari.models import *
 
faker = Faker(["es_CA","es_ES"])
 
class Command(BaseCommand):
    help = 'Productes'
 
    def handle(self, *args, **options):
        # Creem categories
        for i in range(5):
            nova_categoria =  faker.vehicle_category
            categoria= Categoria(nom=nova_categoria)
            categoria.save()
            for j in range(5):
                nou_producte = faker.random_company_product
                producte = Producte(nom=nou_producte, categoria=categoria)
                producte.save()
                # Posem els exemplars
                for k in range(5)
                    nou_exemplar = 
                    exemplar = Exemplar(producte=producte,
                                        estat=
                                        num_serie=
                                        ubicacio=)
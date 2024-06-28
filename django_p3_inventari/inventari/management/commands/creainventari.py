from django.core.management.base import BaseCommand, CommandError
import  random

from faker import Faker
 
from inventari.models import *
from faker_marketdata import MarketDataProvider

faker = Faker()
faker.add_provider(MarketDataProvider)
 
class Command(BaseCommand):
    help = 'Productes'
 
    def handle(self, *args, **options):
        # Creem ubicacions
        for i in range(5):
            novaubicacio = faker.name()
            ubicacio = Ubicacio (nom=novaubicacio)
            ubicacio.save()

        # Creem categories
        for i in range(5):
            nova_categoria =  faker.name()
            categoria= Categoria(nom=nova_categoria)
            categoria.save()
            #Creem productes
            for j in range(5):
                nou_producte = faker.name_nonbinary()
                producte = Producte(nom=nou_producte, categoria=categoria)
                producte.save()
                # Posem els exemplars
                for k in range(5):
                    nouexemplar= faker.isin()
                    novaubicacio= Ubicacio.objects.order_by('?').first()
                    opcionsestat = Exemplar.ESTAT_PRODUCTE
                    # Seleccionar un valor aleatorio
                    estat = random.choice(opcionsestat)[0]
                    exemplar = Exemplar(producte=producte,
                                        estat= estat,
                                        num_serie= nouexemplar,
                                        ubicacio=novaubicacio,
                                        )
                    exemplar.save()
# Generated by Django 4.2 on 2024-06-27 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('descripcio', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Ubicacions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('descripcio', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Producte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('descripcio', models.CharField(max_length=200)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventari.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Exemplars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estat', models.CharField(choices=[('be', 'BÉ'), ('regular', 'REGULAR'), ('dolent', 'DOLENT')], max_length=10)),
                ('num_serie', models.CharField(max_length=30)),
                ('producte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventari.categoria')),
            ],
        ),
    ]
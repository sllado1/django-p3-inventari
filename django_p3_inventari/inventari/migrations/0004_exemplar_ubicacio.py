# Generated by Django 4.2 on 2024-06-28 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventari', '0003_alter_exemplar_producte'),
    ]

    operations = [
        migrations.AddField(
            model_name='exemplar',
            name='ubicacio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventari.ubicacio'),
        ),
    ]

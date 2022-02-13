# Generated by Django 4.0.2 on 2022-02-07 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='name',
            field=models.TextField(help_text='Ingrese el nombre del género (p. ej. Ciencia Ficción, Poesía Francesa etc.)', max_length=200, null=True),
        ),
    ]

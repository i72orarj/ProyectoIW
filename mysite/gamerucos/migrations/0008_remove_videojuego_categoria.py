# Generated by Django 3.0.5 on 2020-04-22 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamerucos', '0007_delete_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videojuego',
            name='categoria',
        ),
    ]

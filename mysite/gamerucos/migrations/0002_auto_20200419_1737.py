# Generated by Django 3.0.5 on 2020-04-19 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamerucos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='critica',
            old_name='videojuegoRespondido',
            new_name='criticaRespondida',
        ),
    ]

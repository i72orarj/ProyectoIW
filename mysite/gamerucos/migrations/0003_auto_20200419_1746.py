# Generated by Django 3.0.5 on 2020-04-19 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gamerucos', '0002_auto_20200419_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='critica',
            name='criticaRespondida',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gamerucos.Critica'),
        ),
    ]

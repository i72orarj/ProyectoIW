# Generated by Django 3.0.5 on 2020-04-22 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gamerucos', '0009_videojuego_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='videojuego',
            name='categoria',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gamerucos.Categoria'),
        ),
    ]

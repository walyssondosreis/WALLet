# Generated by Django 3.2.2 on 2021-05-14 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alvo', '0001_initial'),
        ('valor', '0001_initial'),
        ('operacao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='operacao',
            name='alvo',
            field=models.ManyToManyField(to='alvo.Alvo'),
        ),
        migrations.AddField(
            model_name='operacao',
            name='valor',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='valor.valor'),
        ),
    ]

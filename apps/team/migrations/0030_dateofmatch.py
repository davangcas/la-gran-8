# Generated by Django 3.2.6 on 2021-08-27 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0029_cautions'),
    ]

    operations = [
        migrations.CreateModel(
            name='DateOfMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField(verbose_name='Número de Fecha')),
                ('day_of_match', models.DateField(verbose_name='Fecha de Juego')),
                ('matchs', models.ManyToManyField(to='team.Match')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.tournament')),
            ],
            options={
                'verbose_name': 'Fechas',
            },
        ),
    ]
# Generated by Django 3.1.13 on 2021-08-03 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0009_auto_20210803_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='team.team', verbose_name='Equipo'),
        ),
    ]

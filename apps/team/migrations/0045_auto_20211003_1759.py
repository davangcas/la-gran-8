# Generated by Django 3.2.6 on 2021-10-03 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0044_alter_group_teams'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='goals',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Goles'),
        ),
        migrations.AddField(
            model_name='team',
            name='goals_received',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Goles recibidos'),
        ),
    ]
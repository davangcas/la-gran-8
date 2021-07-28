# Generated by Django 3.1.7 on 2021-07-28 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0003_auto_20210508_2252'),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('title', models.CharField(max_length=80, verbose_name='Título')),
                ('body', models.TextField(max_length=500, verbose_name='Cuerpo')),
                ('image', models.ImageField(blank=True, default='noticias\\default\\Logo Fondo Gris (1).jpeg', null=True, upload_to='noticias/%y/%m/', verbose_name='Imágen')),
            ],
            options={
                'verbose_name': 'Noticia',
                'verbose_name_plural': 'Noticias',
            },
        ),
    ]

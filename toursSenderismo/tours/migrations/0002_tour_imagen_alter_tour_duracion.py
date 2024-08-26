# Generated by Django 5.0.6 on 2024-07-12 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='imagen',
            field=models.ImageField(null=True, upload_to='fotos', verbose_name='Fotografia'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='duracion',
            field=models.IntegerField(),
        ),
    ]
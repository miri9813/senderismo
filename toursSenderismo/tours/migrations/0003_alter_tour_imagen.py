# Generated by Django 5.0.6 on 2024-07-12 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0002_tour_imagen_alter_tour_duracion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='imagen',
            field=models.ImageField(null=True, upload_to='fotos', verbose_name='Fotografía'),
        ),
    ]

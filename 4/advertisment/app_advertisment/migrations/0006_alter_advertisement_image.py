# Generated by Django 4.2.3 on 2023-08-15 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisment', '0005_alter_advertisement_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(blank=True, default=1, upload_to='advertisments/', verbose_name='Изображение'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2.2 on 2023-08-25 04:01

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_banner_banner_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='banner_file',
            field=models.ImageField(default='banners/unknown.jpeg', upload_to=main.models.rename_banner_file, verbose_name='файл баннера'),
        ),
    ]
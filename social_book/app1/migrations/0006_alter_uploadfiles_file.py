# Generated by Django 4.1 on 2023-01-24 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_uploadfiles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfiles',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]
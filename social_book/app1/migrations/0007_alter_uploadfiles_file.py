# Generated by Django 4.1 on 2023-01-24 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_alter_uploadfiles_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfiles',
            name='file',
            field=models.FileField(upload_to='document/'),
        ),
    ]

# Generated by Django 4.1 on 2023-02-04 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0016_customuser_is_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_author',
            field=models.BooleanField(),
        ),
    ]
# Generated by Django 4.1 on 2023-02-04 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0017_alter_customuser_is_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_author',
            field=models.CharField(max_length=100),
        ),
    ]

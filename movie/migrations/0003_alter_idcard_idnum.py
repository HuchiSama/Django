# Generated by Django 4.2 on 2023-09-24 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_idcard_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idcard',
            name='idNum',
            field=models.IntegerField(unique=True),
        ),
    ]

# Generated by Django 4.2 on 2023-09-23 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peplemodel',
            name='uid',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
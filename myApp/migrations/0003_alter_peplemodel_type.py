# Generated by Django 4.2 on 2023-09-23 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_alter_peplemodel_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peplemodel',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.usertype'),
        ),
    ]

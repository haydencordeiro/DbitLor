# Generated by Django 3.1.6 on 2021-02-24 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endpointApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='time',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
    ]

# Generated by Django 3.1.6 on 2021-02-24 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endpointApp', '0006_auto_20210224_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
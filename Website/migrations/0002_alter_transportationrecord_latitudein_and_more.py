# Generated by Django 4.2.7 on 2023-12-26 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transportationrecord',
            name='latitudeIN',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transportationrecord',
            name='latitudeOUT',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transportationrecord',
            name='longitudeIN',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transportationrecord',
            name='longitudeOUT',
            field=models.CharField(blank=True, null=True),
        ),
    ]
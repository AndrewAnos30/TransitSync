# Generated by Django 4.2.7 on 2023-12-26 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0003_alter_transportationrecord_latitudein_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transportationrecord',
            name='penalty',
            field=models.BooleanField(default=False),
        ),
    ]

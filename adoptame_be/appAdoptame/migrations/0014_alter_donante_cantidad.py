# Generated by Django 3.2.7 on 2021-10-31 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appAdoptame', '0013_mascota_personalidades'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donante',
            name='cantidad',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]

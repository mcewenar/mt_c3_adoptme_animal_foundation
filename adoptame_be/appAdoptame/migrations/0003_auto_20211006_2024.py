# Generated by Django 3.2.7 on 2021-10-07 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appAdoptame', '0002_auto_20211006_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='donante',
            name='email',
            field=models.EmailField(default='-', max_length=254),
        ),
        migrations.AlterField(
            model_name='donante',
            name='nombre',
            field=models.CharField(max_length=40),
        ),
    ]

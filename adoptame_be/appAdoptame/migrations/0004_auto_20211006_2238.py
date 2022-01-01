# Generated by Django 3.2.7 on 2021-10-07 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appAdoptame', '0003_auto_20211006_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='donante',
            name='amount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='donante',
            name='transaction_type',
            field=models.CharField(choices=[('C', 'Credit card'), ('D', 'Debit card')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='donante',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='donante',
            name='objetivo',
            field=models.TextField(blank=True, null=True),
        ),
    ]
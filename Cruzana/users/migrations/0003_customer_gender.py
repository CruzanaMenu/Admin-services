# Generated by Django 4.1 on 2022-08-24 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_customers_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[('Masculino', 'Male'), ('Femenino', 'Female')], default='Masculino', max_length=10),
        ),
    ]

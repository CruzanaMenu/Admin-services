# Generated by Django 4.1 on 2022-09-12 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_bebidas_comida_pedidos'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bebidas',
            new_name='Bebida',
        ),
        migrations.RenameModel(
            old_name='Pedidos',
            new_name='Pedido',
        ),
    ]

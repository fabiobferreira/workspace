# Generated by Django 4.1.6 on 2023-02-14 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_cpf_cliente_cpf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='CPF',
        ),
        migrations.DeleteModel(
            name='CPF',
        ),
    ]

# Generated by Django 4.1.6 on 2023-02-14 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0008_departamento_cliente_departamentos'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='foto',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
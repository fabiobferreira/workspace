# Generated by Django 4.1.6 on 2023-02-15 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_parametros'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovRotativo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkin', models.DateTimeField()),
                ('checkout', models.DateTimeField(blank=True)),
                ('valor_hora', models.DecimalField(decimal_places=2, max_digits=6)),
                ('pago', models.BooleanField(default=False)),
                ('veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.veiculo')),
            ],
        ),
    ]

# Generated by Django 2.0.4 on 2018-06-06 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoDeVenta',
            fields=[
                ('idTipoDeVenta', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Tipo de venta',
                'verbose_name_plural': 'Tipos de venta',
            },
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=300)),
                ('stock', models.SmallIntegerField()),
                ('stock_minimo', models.SmallIntegerField()),
                ('costo', models.DecimalField(max_digits=10, decimal_places=2)),
                ('precio_minorista', models.DecimalField(max_digits=10, decimal_places=2)),
                ('precio_mayorista', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
        ),
    ]

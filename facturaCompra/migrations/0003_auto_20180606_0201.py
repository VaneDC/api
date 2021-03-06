# Generated by Django 2.0.4 on 2018-06-06 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_auto_20180606_0105'),
        ('facturaCompra', '0002_auto_20180521_2356'),
    ]

    operations = [
        migrations.CreateModel(
            name='facturaCompraContieneProductos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cantidad', models.IntegerField()),
                ('descuento', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name': 'Factura de compra contiene productos',
                'verbose_name_plural': 'Facturas de compra contiene productos',
            },
        ),
        migrations.AlterModelOptions(
            name='facturacompra',
            options={'verbose_name': 'Factura de compra', 'verbose_name_plural': 'Facturas de compra'},
        ),
        migrations.AddField(
            model_name='facturacompracontieneproductos',
            name='idFacturaCompra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturaCompra.facturaCompra'),
        ),
        migrations.AddField(
            model_name='facturacompracontieneproductos',
            name='idProducto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='productos.Producto'),
        ),
    ]

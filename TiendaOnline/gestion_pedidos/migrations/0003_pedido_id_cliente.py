# Generated by Django 2.2.8 on 2019-12-14 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_pedidos', '0002_auto_20191214_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='id_cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gestion_pedidos.Cliente'),
            preserve_default=False,
        ),
    ]

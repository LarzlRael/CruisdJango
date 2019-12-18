# Generated by Django 2.2.8 on 2019-12-14 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_pedidos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('fecha', models.DateField()),
                ('entrada', models.BooleanField()),
                ('salida', models.BooleanField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Articulos',
            new_name='Articulo',
        ),
        migrations.RenameModel(
            old_name='Clientes',
            new_name='Cliente',
        ),
        migrations.RenameModel(
            old_name='Pedidos',
            new_name='Pedido',
        ),
        migrations.RenameField(
            model_name='pedido',
            old_name='entreado',
            new_name='entrada',
        ),
    ]
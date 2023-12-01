# Generated by Django 4.2.7 on 2023-12-01 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.CharField(max_length=255, unique=True, verbose_name='Codigo de Barras')),
                ('name', models.CharField(help_text='Nombre', max_length=255)),
                ('descripcion', models.TextField(blank=True, help_text='Descripcion del producto', null=True)),
                ('price', models.DecimalField(decimal_places=2, help_text='Precio del producto', max_digits=20)),
                ('created_at', models.DateTimeField(auto_now=True, help_text='Fecha de creación del objeto')),
                ('updated_at', models.DateTimeField(auto_now_add=True, help_text='Fecha de creación del objeto')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'db_table': 'product',
                'ordering': ('-id',),
            },
        ),
    ]
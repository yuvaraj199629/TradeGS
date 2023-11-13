# Generated by Django 4.2.6 on 2023-11-01 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=200)),
                ('item_group', models.CharField(max_length=200)),
                ('acc', models.CharField(max_length=200)),
                ('mrp', models.CharField(max_length=200)),
                ('open_stock', models.CharField(max_length=200)),
                ('unit', models.CharField(max_length=200)),
                ('tax', models.CharField(max_length=200)),
                ('hSN', models.CharField(max_length=200)),
                ('purchase_rate', models.CharField(max_length=200)),
                ('retail_rate', models.CharField(max_length=200)),
                ('ws_rate', models.CharField(max_length=200)),
                ('qty_rate', models.CharField(max_length=200)),
                ('bluk_unit', models.CharField(max_length=200)),
                ('Cess', models.CharField(max_length=200)),
                ('bulk_qty', models.CharField(max_length=200)),
                ('cess_price', models.CharField(max_length=200)),
            ],
        ),
    ]

# Generated by Django 4.2.6 on 2023-11-04 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0002_party'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_id', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
                ('customer', models.CharField(max_length=200)),
                ('amount', models.CharField(max_length=200)),
                ('adj', models.CharField(max_length=200)),
                ('remark', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_id', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
                ('supplier', models.CharField(max_length=200)),
                ('amount', models.CharField(max_length=200)),
                ('adj', models.CharField(max_length=200)),
                ('remark', models.CharField(max_length=200)),
            ],
        ),
    ]

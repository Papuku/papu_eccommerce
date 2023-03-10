# Generated by Django 4.1.4 on 2023-01-09 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_name', models.CharField(max_length=50)),
                ('product_name', models.CharField(max_length=50)),
                ('product_price', models.FloatField(max_length=50)),
                ('discount', models.CharField(max_length=10)),
                ('GST', models.CharField(max_length=50)),
                ('mobile_number', models.CharField(max_length=15)),
                ('selle_address', models.TextField(max_length=500)),
                ('discription', models.TextField(max_length=800)),
                ('image', models.FileField(upload_to='')),
            ],
        ),
    ]

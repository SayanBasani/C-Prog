# Generated by Django 5.0.6 on 2024-07-07 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0002_seller_singup_type_seller_singup_product_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('option', models.CharField(max_length=50)),
                ('product_id', models.CharField(max_length=100, unique=True)),
                ('product_img', models.URLField()),
                ('product_count', models.IntegerField()),
                ('seller_id', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=50)),
                ('fabric', models.CharField(max_length=100)),
                ('design', models.CharField(max_length=100)),
                ('patterns', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=50)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Gadget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('option', models.CharField(max_length=50)),
                ('product_id', models.CharField(max_length=100, unique=True)),
                ('product_img', models.URLField()),
                ('product_count', models.IntegerField()),
                ('seller_id', models.CharField(max_length=100)),
                ('battery_present', models.BooleanField()),
                ('chargeable', models.BooleanField()),
                ('brand', models.CharField(max_length=100)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('model_number', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=50)),
                ('wireless_connection', models.CharField(max_length=100)),
                ('battery_type', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('option', models.CharField(max_length=50)),
                ('product_id', models.CharField(max_length=100, unique=True)),
                ('product_img', models.URLField()),
                ('product_count', models.IntegerField()),
                ('seller_id', models.CharField(max_length=100)),
                ('display_size', models.CharField(max_length=50)),
                ('display', models.CharField(max_length=100)),
                ('battery', models.CharField(max_length=100)),
                ('network', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('ram_rom', models.CharField(max_length=100)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('camera', models.CharField(max_length=100)),
                ('processors', models.CharField(max_length=100)),
                ('warranty', models.CharField(max_length=100)),
                ('model_number', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=50)),
                ('sim_slot', models.CharField(max_length=50)),
                ('wifi', models.CharField(max_length=100)),
                ('battery_type', models.CharField(max_length=100)),
                ('graphics', models.CharField(max_length=100)),
                ('charging', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('option', models.CharField(max_length=50)),
                ('product_id', models.CharField(max_length=100, unique=True)),
                ('product_img', models.URLField()),
                ('product_count', models.IntegerField()),
                ('seller_id', models.CharField(max_length=100)),
                ('display_size', models.CharField(max_length=50)),
                ('display', models.CharField(max_length=100)),
                ('battery', models.CharField(max_length=100)),
                ('network', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('ram_rom', models.CharField(max_length=100)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('camera', models.CharField(max_length=100)),
                ('processors', models.CharField(max_length=100)),
                ('warranty', models.CharField(max_length=100)),
                ('model_number', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=50)),
                ('sim_slot', models.CharField(max_length=50)),
                ('wifi', models.CharField(max_length=100)),
                ('battery_type', models.CharField(max_length=100)),
                ('graphics', models.CharField(max_length=100)),
                ('charging', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('main_id', models.CharField(max_length=100, unique=True)),
                ('product_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Shoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('option', models.CharField(max_length=50)),
                ('product_id', models.CharField(max_length=100, unique=True)),
                ('product_img', models.URLField()),
                ('product_count', models.IntegerField()),
                ('seller_id', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=50)),
                ('fabric', models.CharField(max_length=100)),
                ('design', models.CharField(max_length=100)),
                ('patterns', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=50)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Toy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('option', models.CharField(max_length=50)),
                ('product_id', models.CharField(max_length=100, unique=True)),
                ('product_img', models.URLField()),
                ('product_count', models.IntegerField()),
                ('seller_id', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('chargeable', models.BooleanField()),
                ('size', models.CharField(max_length=50)),
                ('material', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
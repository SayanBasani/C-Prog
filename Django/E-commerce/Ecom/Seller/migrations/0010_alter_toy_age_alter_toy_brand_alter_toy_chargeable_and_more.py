# Generated by Django 5.0.6 on 2024-07-10 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0009_all_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toy',
            name='age',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='toy',
            name='brand',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='toy',
            name='chargeable',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='toy',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='toy',
            name='material',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='toy',
            name='model',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='toy',
            name='price',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='toy',
            name='product_img',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='toy',
            name='size',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='toy',
            name='type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='toy',
            name='user',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='toy',
            name='weight',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
# Generated by Django 3.1.5 on 2021-08-12 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_products_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_id',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]

# Generated by Django 3.2.6 on 2021-08-21 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0036_auto_20210821_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products_intheinventory',
            name='buy_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='products_intheinventory',
            name='num_of_items',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='products_intheinventory',
            name='sell_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=19, null=True),
        ),
    ]
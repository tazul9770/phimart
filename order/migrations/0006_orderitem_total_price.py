# Generated by Django 5.1.6 on 2025-03-04 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=100.0, max_digits=10),
            preserve_default=False,
        ),
    ]

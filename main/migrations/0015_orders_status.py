# Generated by Django 4.0.6 on 2022-10-20 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_orders_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out For Delivary', 'Out For Delivary'), ('Delivered', 'Delivered')], default='Pending', max_length=190),
        ),
    ]

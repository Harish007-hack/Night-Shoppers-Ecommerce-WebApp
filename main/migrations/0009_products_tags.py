# Generated by Django 4.0.6 on 2022-10-20 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_products_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='tags',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
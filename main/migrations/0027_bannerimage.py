# Generated by Django 4.0.6 on 2022-12-13 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_rename_buyer_orders_buyer'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bannerPic', models.ImageField(blank=True, error_messages={'invalid': 'Image files only'}, null=True, upload_to='')),
            ],
        ),
    ]
# Generated by Django 5.1 on 2024-09-14 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_disciptions_product_valume'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
    ]

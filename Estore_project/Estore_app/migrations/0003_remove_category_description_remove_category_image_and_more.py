# Generated by Django 4.1.4 on 2023-01-07 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Estore_app', '0002_category_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
        migrations.RemoveField(
            model_name='category',
            name='price',
        ),
    ]

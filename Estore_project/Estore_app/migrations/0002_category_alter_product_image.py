# Generated by Django 4.1.4 on 2023-01-07 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Estore_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('description', models.CharField(default='', max_length=200)),
                ('image', models.ImageField(upload_to='upload/products/')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='upload/products/'),
        ),
    ]

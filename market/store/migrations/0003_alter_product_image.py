# Generated by Django 4.2 on 2023-07-25 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='store/static/store/img/%Y/%m/%d'),
        ),
    ]

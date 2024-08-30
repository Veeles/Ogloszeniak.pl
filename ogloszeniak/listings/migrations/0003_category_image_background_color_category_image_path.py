# Generated by Django 4.2.14 on 2024-08-30 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_rename_listings_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image_background_color',
            field=models.TextField(default='black'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='image_path',
            field=models.ImageField(default='static/photos/categoriesIcons/freeitems', upload_to=''),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.0.7 on 2024-08-05 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0002_category_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="image",
            field=models.ImageField(upload_to=""),
        ),
    ]

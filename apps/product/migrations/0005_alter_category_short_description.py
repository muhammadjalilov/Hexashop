# Generated by Django 5.0.7 on 2024-08-05 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0004_alter_category_options_category_short_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="short_description",
            field=models.CharField(max_length=512),
        ),
    ]

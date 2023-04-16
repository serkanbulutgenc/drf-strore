# Generated by Django 4.2 on 2023-04-15 22:04

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0003_alter_product_original_price_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="categories",
            field=mptt.fields.TreeForeignKey(
                help_text="Product Categories",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="categories",
                to="product.category",
            ),
        ),
    ]

# Generated by Django 4.2 on 2023-04-15 21:46

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0002_rename_price_product_original_price_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="original_price",
            field=models.DecimalField(
                decimal_places=2,
                help_text="Product Price",
                max_digits=6,
                verbose_name="Original Price",
            ),
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Category Name", max_length=50, verbose_name="Name"
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        help_text="Category Slug", unique=True, verbose_name="Slug"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="Updated At")),
                ("lft", models.PositiveIntegerField(editable=False)),
                ("rght", models.PositiveIntegerField(editable=False)),
                ("tree_id", models.PositiveIntegerField(db_index=True, editable=False)),
                ("level", models.PositiveIntegerField(editable=False)),
                (
                    "parent",
                    mptt.fields.TreeForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="children",
                        to="product.category",
                    ),
                ),
            ],
            options={
                "verbose_name": "Category",
                "verbose_name_plural": "Categories",
                "ordering": ["-created_at"],
            },
        ),
    ]

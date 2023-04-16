import factory

# from store.apps.product.models import Product


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "product.Product"

    title = factory.Faker("sentence")
    description = factory.Faker("paragraph", nb_sentences=30)
    qty = factory.Faker("pyint")
    original_price = factory.Faker(
        "pyfloat",
        left_digits=4,
        right_digits=2,
        positive=True,
        min_value=0.1,
        max_value=9999.99,
    )
    sale_price = factory.Faker(
        "pyfloat",
        left_digits=4,
        right_digits=2,
        positive=True,
        min_value=0.1,
        max_value=9999.99,
    )
    is_active = factory.Faker("pybool")

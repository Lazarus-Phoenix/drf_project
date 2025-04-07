import stripe
from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_price(amount):
    """Создает цену в stripe"""
    return stripe.Price.create(
        currency="rub",
        unit_amount= int(amount * 100),
        product_data={"name": "Payment"},
    )


def create_stripe_product(product):
    """Создает продукт в stripe"""
    return stripe.Product.create(name=product)


def create_stripe_session(price):
    """Создает сессию на оплату в stripe"""

    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/lms/lessons/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")

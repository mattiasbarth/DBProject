import datetime as dt
from typing import Optional

from Data.models.ordered_products import OrderedProduct
from Data.models.orders import Order
from Data.db import session


def create(**kwargs):
    # TODO: Use default in model
    kwargs['date_created'] = dt.datetime.utcnow()
    order = Order(**kwargs)  # TODO: Check if order could be created
    session.add(order)
    session.commit()
    return order


def edit(order: Order) -> Optional[Order]:
    pass


def find(order_id: int) -> Optional[Order]:
    return session.query(Order).filter_by(id=order_id).one_or_none()


def add_products(*products, order: Order):
    for product in products:
        add_product(product, order)


def add_product(product, order: Order) -> OrderedProduct:
    ordered_product: OrderedProduct = OrderedProduct(
        order_id=order.id,
        product_id=product[0],
        product_amount=product[1],
    )
    session.add(ordered_product)
    session.commit()
    return ordered_product


def remove(order: Order):
    session.delete(order)
    session.commit()

from menu import products
from collections import Counter


def get_product_by_id(id: int) -> dict:
    if type(id) != int:
        raise TypeError("product id must be an int")

    for id_products in products:
        if id_products["_id"] == id:
            return id_products
    return {}


def get_products_by_type(prod_type: str) -> list:
    if type(prod_type) != str:
        raise TypeError("product type must be a str")

    list_products = []

    for type_products in products:
        if type_products["type"] == prod_type:
            list_products.append(type_products)

    return list_products


def add_product(menu: list[dict], **kwargs: dict) -> dict:
    list_id = []

    if len(menu) == 0:
        kwargs["_id"] = 1
        menu.append(kwargs)
        return kwargs

    for id_menu in menu:
        list_id.append(id_menu["_id"])

    max_id_menu = max(list_id)

    if len(menu) > 0:
        kwargs["_id"] = max_id_menu + 1
        menu.append(kwargs)
        return kwargs


def menu_report() -> str:
    count_product = len(products)
    list_price = []
    type_product = []

    for average in products:
        list_price.append(average["price"])
        type_product.append(average["type"])

    type_product = Counter(type_product)
    average_price = round(sum(list_price) / count_product, 2)

    for product in type_product:
        return f"Products Count: {count_product} - Average Price: ${average_price} - Most Common Type: {product}"

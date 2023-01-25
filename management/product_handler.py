from menu import products


def get_product_by_id(id: int):
    if type(id) != int:
        return {}

    for id_products in products:
        if id_products["_id"] == id:
            return id_products
    return {}


def get_products_by_type(prod_type: str):
    if type(prod_type) != str:
        return []

    list_products = []
    for type_products in products:
        if type_products["type"] == prod_type:
            list_products.append(type_products)

    return list_products

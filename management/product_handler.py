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


def add_product(menu, **kwargs):
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

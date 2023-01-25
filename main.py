from management import get_product_by_id, get_products_by_type
from menu import products


def looping_Id():
    for id_products in products:
        get_product_by_id(id_products["_id"])


def looping_type():
    for type_products in products:
        get_products_by_type(type_products["type"])


if __name__ == "__main__":
    # Seus prints de teste aqui
    print(looping_Id())
    print(looping_type())
    ...

from management import get_product_by_id, get_products_by_type, add_product, calculate_tab
from menu import products


new_product = {
    "title": "X-java",
    "price": 5.0,
    "rating": 5,
    "description": "Sanduiche de java",
    "type": "fast-food"
}

table_1 = [{"_id": 1, "amount": 5}, {"_id": 19, "amount": 5}]
table_2 = [
    {"_id": 10, "amount": 3},
    {"_id": 20, "amount": 2},
    {"_id": 21, "amount": 5},
]


def looping_Id():
    for id_products in products:
        get_product_by_id(id_products["_id"])


def looping_type():
    for type_products in products:
        get_products_by_type(type_products["type"])


if __name__ == "__main__":
    # Seus prints de teste aqui
    # print(looping_Id())
    # print(looping_type())
    # print(add_product(products, **new_product))
    # print(calculate_tab(table_1))
    print(calculate_tab(table_2))

    ...

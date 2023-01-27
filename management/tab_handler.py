from menu import products


def calculate_tab(orders: dict) -> dict:
    sum_value = 0
    for order in orders:
        for product in products:
            if product["_id"] == order["_id"]:
                sum_value += product["price"] * order["amount"]
    return {"subtotal": f"${round(sum_value, 2)}"}

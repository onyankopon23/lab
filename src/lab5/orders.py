class Order:
    def __init__(self, number, products, name, address, phone, priority):
        self.number = number
        self.products = products
        self.name = name
        self.address = address
        self.phone = phone
        self.priority = priority


def check_address(address):
    if address == "":
        return False
    parts = address.split(". ")
    if len(parts) != 4:
        return False

    return True


def check_phone(phone):
    if phone == "":
        return False
    parts = phone.split("-")
    if len(parts) != 5:
        return False
    if len(parts[0]) != 2:
        return False
    if parts[0][0] != "+":
        return False
    if not parts[0][1].isdigit():
        return False
    if len(parts[1]) != 3 or not parts[1].isdigit():
        return False
    if len(parts[2]) != 3 or not parts[2].isdigit():
        return False
    if len(parts[3]) != 2 or not parts[3].isdigit():
        return False
    if len(parts[4]) != 2 or not parts[4].isdigit():
        return False

    return True


def format_products(products):
    products_list = products.split(", ")
    res = []
    used = []
    for product in products_list:
        if product not in used:
            cnt = products_list.count(product)
            if cnt > 1:
                res.append(product + " x" + str(cnt))
            else:
                res.append(product)
            used.append(product)

    return ", ".join(res)


def get_country(address):
    parts = address.split(". ")
    return parts[0]


def remove_country(address):
    parts = address.split(". ")
    return ". ".join(parts[1:])


def get_priority(priority):
    if priority == "MAX":
        return 1
    elif priority == "MIDDLE":
        return 2
    else:
        return 3


def read_orders(filename):
    orders = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue
            parts = line.split(";")
            order = Order(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5])
            orders.append(order)

        return orders


def validate_orders(orders):
    valid_orders = []
    errors = []
    for order in orders:
        is_error = False
        if not check_phone(order.phone):
            if order.phone == "":
                errors.append([order.number, "2", "no data"])
            else:
                errors.append([order.number, "2", order.phone])
            is_error = True
        if not check_address(order.address):
            if order.address == "":
                errors.append([order.number, "1", "no data"])
            else:
                errors.append([order.number, "1", order.address])
            is_error = True
        if not is_error:
            valid_orders.append(order)

    return valid_orders, errors


def sort_key(order):
    country = get_country(order.address)
    priority = get_priority(order.priority)
    if country == "Россия":
        country = ""

    return country, priority


def sort_orders(orders):
    return sorted(orders, key=sort_key)


def save_errors(errors, filename):
    with open(filename, "w", encoding="utf-8") as file:
        for error in errors:
            file.write(";".join(error) + "\n")


def save_orders(orders, filename):
    with open(filename, "w", encoding="utf-8") as file:
        for order in orders:
            products = format_products(order.products)
            address = remove_country(order.address)
            line = (order.number + ";" + products + ";" + order.name + ";" + address + ";" + order.phone + ";" + order.priority)

            file.write(line + "\n")


def main():
    orders = read_orders("orders.txt")
    valid_orders, errors = validate_orders(orders)
    valid_orders = sort_orders(valid_orders)

    save_orders(valid_orders, "order_country.txt")
    save_errors(errors, "non_valid_orders.txt")


if __name__ == "__main__":
    main()

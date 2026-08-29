import unittest

from src.lab5.orders import (
    Order,
    check_phone,
    check_address,
    format_products,
    sort_orders
)



class OrdersTestCase(unittest.TestCase):
    def test_check_address_valid(self):
        address = "Россия. Московская область. Москва. улица Пушкина"
        res = check_address(address)
        self.assertTrue(res)

    def test_check_address_invalid(self):
        address = "Япония. Шибуя. Шибуя-кроссинг"
        res = check_address(address)
        self.assertFalse(res)

    def test_check_address_empty(self):
        address = ""
        res = check_address(address)
        self.assertFalse(res)

    def test_check_phone_valid(self):
        phone = "+7-912-345-67-89"
        res = check_phone(phone)
        self.assertTrue(res)

    def test_check_phone_invalid(self):
        phone = "+4-989-234-56"
        res = check_phone(phone)
        self.assertFalse(res)

    def test_check_phone_empty(self):
        phone = ""
        res = check_phone(phone)
        self.assertFalse(res)

    def test_format_products(self):
        products = "Сыр, Колбаса, Сыр, Макароны, Колбаса"
        res = format_products(products)
        self.assertEqual(res, "Сыр x2, Колбаса x2, Макароны")

    def test_sort_orders(self):
        order1 = Order(
            "1",
            "Хлеб",
            "Иванов Иван",
            "Франция. Регион. Париж. Улица",
            "+3-111-111-11-11",
            "MIDDLE"
        )
        order2 = Order(
            "2",
            "Молоко",
            "Петров Петр",
            "Россия. Регион. Москва. Улица",
            "+7-111-111-11-11",
            "MAX"
        )
        order3 = Order(
            "3",
            "Сыр",
            "Сидоров Сидор",
            "Великобритания. Регион. Лондон. Улица",
            "+4-111-111-11-11",
            "LOW"
        )
        orders = [order1, order2, order3]
        res = sort_orders(orders)
        self.assertEqual(res[0].number, "2")
        self.assertEqual(res[1].number, "3")
        self.assertEqual(res[2].number, "1")




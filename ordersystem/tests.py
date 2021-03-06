from unittest import skipIf

from django.test import TestCase

from ordersystem.models import \
    CustomerAccount, \
    UserAccount, \
    Cart


class UserAccountTest(TestCase):
    def setUp(self):
        self.user1 = UserAccount(
            first_name="cust",
            last_name="one",
            username="custOne",
            email="cust1@test.com",
            password="1111")

    def test_change_first_name(self):
        self.user1.change_first_name("customer")
        self.assertEqual(self.user1.first_name, "customer")

    def test_change_last_name(self):
        self.user1.change_last_name("ONE")
        self.assertEqual(self.user1.last_name, "ONE")

    def test_change_email(self):
        self.user1.change_email("customerTheFirst@yo.co")
        self.assertEqual(self.user1.email, "customerTheFirst@yo.co")


class CartTest(TestCase):
    def setUp(self):
        self.user2 = CustomerAccount(
            first_name="cust",
            last_name="two",
            username="custTwo",
            email="cust2@test.com",
            password="2222")

        self.user3 = CustomerAccount(
            first_name="cust",
            last_name="three",
            username="custThree",
            email="cust3@test.com",
            password="3333")

    def test_only_one_cart_per_customer(self):
        self.cart1 = Cart(customer=self.user2)
        self.cart2 = Cart(customer=self.user2)
        self.assertRaises(ValueError)

    def test_only_one_customer_per_cart(self):
        self.cart1 = Cart(customer=self.user2)
        self.cart1.customer = self.user3
        self.assertEqual(self.cart1.customer, self.user3)

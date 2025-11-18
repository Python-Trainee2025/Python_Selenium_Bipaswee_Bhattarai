import pytest
import time
from selenium.webdriver.common.by import By

from page_objects_assignment.cartpom.cartpage import CartPage
from setup.basetest import BaseTest
from page_objects_assignment.loginpom.login_page import LoginPage
from page_objects_assignment.productpom.productpage import ProductPage


@pytest.mark.parametrize("username", ["standard_user", "problem_user", "performance_glitch_user"])

class TestLogin(BaseTest):
    def test_demo_login_basetest(self, username):
        login=LoginPage(self.driver)
        self.driver.get("https://www.saucedemo.com/")
        time.sleep(3)
        print("Page Title: ", self.driver.title)

        #login
        login.login(username,'secret_sauce')
        print("Username and password entered successfully")

        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(3)

        #add products

        product_page = ProductPage(self.driver)
        product_page.add_product1_to_cart()
        product_page.add_product2_to_cart()
        time.sleep(2)
        print("Products added to cart page")

        #view cart items
        product_page.go_to_cart()
        time.sleep(2)
        print("Cart items viewed")

        # remove items from cart
        cart_page = CartPage(self.driver)
        cart_page.remove_item()
        time.sleep(2)
        print("Cart items removed")

        #go back to the page
        cart_page.continue_shopping()
        time.sleep(2)
        print("Went back to the page")

        #view new item to cart
        product_page.view_item()
        time.sleep(2)
        print("New item viewed")

        #add new item to cart
        product_page.add_new_product()
        time.sleep(2)
        print("New items added")


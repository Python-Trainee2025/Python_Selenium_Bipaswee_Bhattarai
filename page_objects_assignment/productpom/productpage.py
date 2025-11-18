from selenium.webdriver.support.wait import WebDriverWait

from page_objects_assignment.productpom.productlocators import ProductLocators
from page_objects_assignment.productpom.productprops import ProductPageProperties


class ProductPage(ProductPageProperties):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    def add_product1_to_cart(self):
        self.driver.find_element(*ProductLocators.ADD_BACKPACK).click()

    def add_product2_to_cart(self):
        self.driver.find_element(*ProductLocators.ADD_BIKE_LIGHT).click()

    def view_item(self):
        self.driver.find_element(*ProductLocators.ITEM_TITLE_LINK).click()

    def go_to_cart(self):
        self.driver.find_element(*ProductLocators.CART_ICON).click()

    def add_new_product(self):
        self.driver.find_element(*ProductLocators.ADD_NEW_ITEM).click()

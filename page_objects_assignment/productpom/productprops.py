from page_objects_assignment.productpom.productlocators import ProductLocators

class ProductPageProperties(ProductLocators):

    def __init__(self):
        self.driver = None

    def add_backpack(self):
        return self.driver.find_element(*ProductLocators.ADD_BACKPACK)

    def add_bike_light(self):
        return self.driver.find_element(*ProductLocators.ADD_BIKE_LIGHT)

    def cart_icon(self):
        return self.driver.find_element(*ProductLocators.CART_ICON)

    def item_link(self):
        return self.driver.find_element(*ProductLocators.ITEM_TITLE_LINK)

    def add_new_item(self):
        return self.driver.find_element(*ProductLocators.ADD_NEW_ITEM)



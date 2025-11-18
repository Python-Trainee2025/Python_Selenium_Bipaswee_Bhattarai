from page_objects_assignment.cartpom.cartlocators import CartLocators

class CartPageProperties(CartLocators):
    def __init__(self):
        self.driver = None

    def remove_backpack(self):
        return self.driver.find_element(*ProductLocators.REMOVE_BACKPACK)

    def continue_shopping(self):
        return self.driver.find_element(*ProductLocators.CONTINUE_SHOPPING)
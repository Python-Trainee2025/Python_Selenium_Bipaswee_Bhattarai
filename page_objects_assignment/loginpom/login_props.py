from page_objects_assignment.loginpom.login_locators import LoginLocators


class LoginPageProperties(LoginLocators):

    def __init__(self):
        self.driver = None

    @property
    def username_input(self):
        return self.driver.find_element(*LoginLocators.USERNAME_INPUT)

    def password_input(self):
        return self.driver.find_elemnet(*LoginLocators.PASSWORD_INPUT)

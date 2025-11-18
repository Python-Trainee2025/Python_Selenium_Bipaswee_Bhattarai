from selenium.webdriver.support.wait import WebDriverWait

from page_objects_assignment.loginpom.login_props import LoginPageProperties


class LoginPage(LoginPageProperties):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def login(self, username,password):
        self.driver.find_element(*LoginPageProperties.USERNAME_INPUT).send_keys(username)

        self.driver.find_element(*LoginPageProperties.PASSWORD_INPUT).send_keys(password)


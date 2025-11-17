import time
from logging import exception

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

@pytest.mark.parametrize("username", ["standard_user","problem_user","performance_glitch_user"])


def test_demo(username):
    chrome_options=Options()

    driver=webdriver.Chrome(options=chrome_options)

    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    print("Page Title: ", driver.title)
    driver.find_element(By.ID,"user-name").send_keys(username)
    driver.find_element(By.ID,"password").send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    wait = WebDriverWait(driver, 10)
    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "title")))


# add items to cart
    driver.find_element(By.XPATH,'.//button[@id="add-to-cart-sauce-labs-backpack"]').click()
    driver.find_element(By.XPATH, './/button[@id="add-to-cart-sauce-labs-bike-light"]').click()
    wait = WebDriverWait(driver, 10)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "button[id*='add-to-cart']")))

#view cart items
    driver.find_element(By.ID,"shopping_cart_container").click()

# remove items from cart
    driver.find_element(By.XPATH, './/button[@id="remove-sauce-labs-backpack"]').click()
    wait = WebDriverWait(driver, 10)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "button[id*='remove']")))

# go back to the page
    driver.find_element(By.ID, "continue-shopping").click()
    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "inventory_item")))

#view new item
    driver.find_element(By.ID,"item_1_title_link").click()

    #add new item to cart
    driver.find_element(By.XPATH, './/BUTTON[@id="add-to-cart"]').click()
    driver.quit()

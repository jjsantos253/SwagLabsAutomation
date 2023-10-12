from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.title = (By.XPATH, "//span[contains(@class,'title')][text()='Products']")
        self.error_message = (By.CSS_SELECTOR, "[data-test='error']")

    def add_credentials(self, username, password):
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)

    def is_logged_in(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.title))
            return True
        except:
            return False

    def is_error_message_displayed(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.error_message))
            return True
        except:
            return False

    def go_to_login_page(self):
        self.driver.get("https://www.saucedemo.com/")

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def get_error_message(self):
        try:
            element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.error_message))
            return element.text
        except:
            return None

    def is_on_login(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.login_button))
            return True
        except:
            return False

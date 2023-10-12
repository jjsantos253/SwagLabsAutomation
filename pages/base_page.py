from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.side_menu = (By.ID, "react-burger-menu-btn")
        self.logout_button = (By.ID, "logout_sidebar_link")

    def click_logout(self):
        element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.logout_button))
        element.click()

    def click_side_menu(self):
        self.driver.find_element(*self.side_menu).click()

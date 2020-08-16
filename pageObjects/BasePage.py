from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class BasePage():
    """This class is the parent class for all the pages in our application."""
    """It contains all common elements and functionalities available to all pages."""

    # this function is called every time a new object of the base class is created.
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    # this function performs click on web element whose locator is passed to it.
    def click(self, by_locator):
        self.wait.until(EC.element_to_be_clickable(by_locator)).click()

    # this function performs clear on web element whose locator is passed to it.
    def clear(self, by_locator):
        self.wait.until(EC.visibility_of_element_located(by_locator)).clear()

    # this function performs text entry of the passed in text, in a web element whose locator is passed to it.
    def enter_text(self, by_locator, text):
        return self.wait.until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    # this function checks if the web element whose locator has been passed to it, is visible or not and returns
    # true or false depending upon its visibility.
    def is_visible(self, by_locator):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    # this function returns the title of a page
    def get_title(self):
        return self.driver.title

    # this function returns list of web elements found
    def get_element_list(self, by_locator):
        return self.wait.until(EC.visibility_of_all_elements_located(by_locator))

    # this function returns text of a web element found
    def get_text(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator)).text

    # this function returns a link's text
    def get_link_text(self, value):
        return self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, value)))

    # this function returns list of a drop down options
    def get_drop_down_list_options(self, by_locator):
        return Select(self.wait.until(EC.element_to_be_clickable(by_locator))).options

    # this function captures a screenshot with given filename
    def save_screenshot(self, filename):
        self.driver.save_screenshot(".\\Screenshots\\" + filename + ".png")

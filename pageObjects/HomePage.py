from utilities.locators import *
from pageObjects.BasePage import BasePage


class HomePage(BasePage):
    """Home Page of imdb.com"""

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = HomePageLocators

    def click_on_menu(self):
        self.click(self.locators.BTN_MENU)

    def click_on_top_rated_movies(self):
        self.click(self.locators.LNK_TOP_RATED_MOVIES)


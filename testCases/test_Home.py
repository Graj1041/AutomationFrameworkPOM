import pytest
from pageObjects.HomePage import HomePage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Home:

    logger = LogGen.log_gen()
    baseURL = ReadConfig.getApplicationURL()

    @pytest.fixture()
    def setup(self, setupDriver):
        self.driver = setupDriver
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.hp = HomePage(self.driver)
        yield
        self.driver.close()

    def test_homePageTitle(self, setup):
        self.logger.info("****** Test_001_Home Starts Here******")
        self.logger.info("****** verifying home Page Title ******")
        if self.driver.title == "IMDb: Ratings, Reviews, and Where to Watch the Best Movies & TV Shows":
            assert True
            self.logger.info("****** home Page Title is passed ******")
        else:
            self.save_screenshot("test_homePageTitle")
            self.logger.error("****** home Page Title is failed ******")
            assert False

    def test_homePageMenu(self, setup):
        self.logger.info("****** verifying home Page Menu ******")
        self.hp.click_on_menu()
        self.hp.click_on_top_rated_movies()
        if self.driver.title == "IMDb Top 250 - IMDb":
            assert True
            self.logger.info("******  Home Page Menu is Passed ******")
        else:
            self.save_screenshot("test_homePageMenu")
            self.logger.error("****** Home Page Menu is Failed ******")
            assert False

import pytest
from pageObjects.HomePage import HomePage
from pageObjects.MovieListPage import MovieListPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_MoviePageDetails:

    logger = LogGen.log_gen()
    baseURL = ReadConfig.getApplicationURL()

    @pytest.fixture()
    def setup(self, setupDriver):
        self.driver = setupDriver
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.hp = HomePage(self.driver)
        self.hp.click_on_menu()
        self.hp.click_on_top_rated_movies()
        self.mlp = MovieListPage(self.driver)
        yield
        self.driver.close()

    def test_Top250MoviePageTitle(self, setup):
        self.logger.info("****** Test_001_MovieListOrder ******")
        self.logger.info("****** verifying Top 250 Movie Page Title ******")
        if self.driver.title == "IMDb Top 250 - IMDb":
            assert True
            self.logger.info("****** Top 250 Movie Page Title is passed ******")
        else:
            self.mlp.save_screenshot("test_Top250MoviePageTitle")
            self.logger.error("****** Top 250 Movie Page Title is failed ******")
            assert False

    def test_orderChangeOfMovies(self, setup):
        self.logger.info("****** Verifying order Change Of Movies List ******")
        movie_list_before = self.mlp.get_top_n_movie_list(250)
        self.mlp.change_order_of_movie_list()
        movie_list_after = self.mlp.get_top_n_movie_list(250)
        if movie_list_before == movie_list_after[::-1]:
            assert True
            self.logger.info("******  Movie List order change is passed ******")
        else:
            self.mlp.save_screenshot("test_orderChangeOfMovies")
            self.logger.error("****** Movie List order change is failed ******")
            assert False


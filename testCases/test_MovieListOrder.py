import pytest
from pageObjects.HomePage import HomePage
from pageObjects.MovieListPage import MovieListPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_MovieListOrder:

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
        self.list_actual_movies_details = self.mlp.get_details_of_movies()
        yield
        self.driver.close()

    def test_sortingOfMoviesListByIMDbRating(self, setup):
        self.logger.info("****** Verifying Sorting Of Movies List ******")
        self.mlp.sort_movie_list_by('IMDb Rating')
        list_sorted_movies = self.mlp.get_top_n_movie_list()
        self.list_actual_movies_details.sort(key=lambda x: x['IMDb Rating'], reverse=True)
        list_actual_movies = [movDict['Movie Name'] for movDict in self.list_actual_movies_details]
        if list_actual_movies == list_sorted_movies:
            assert True
            self.logger.info("******  Verifying Sorting Of Movies List by IMDb Rating is passed ******")
        else:
            self.mlp.save_screenshot("test_sortingOfMoviesListByIMDbRating")
            self.logger.info("******  Verifying Sorting Of Movies List by IMDb Rating is failed ******")
            assert False

    def test_sortingOfMoviesListByNumberOfRatings(self, setup):
        self.logger.info("****** Verifying Sorting Of Movies List ******")
        self.mlp.sort_movie_list_by('Number of Ratings')
        list_sorted_movies = self.mlp.get_top_n_movie_list()
        self.list_actual_movies_details.sort(key=lambda x: x['Number of Ratings'], reverse=True)
        list_actual_movies = [movDict['Movie Name'] for movDict in self.list_actual_movies_details]
        if list_actual_movies == list_sorted_movies:
            assert True
            self.logger.info("******  Verifying Sorting Of Movies List by Number Of Ratings is passed ******")
        else:
            self.mlp.save_screenshot("test_sortingOfMoviesListByNumberOfRatings")
            self.logger.info("******  Verifying Sorting Of Movies List by Number Of Ratings is failed ******")
            assert False

    def test_sortingOfMoviesListByReleaseDate(self, setup):
        self.logger.info("****** Verifying Sorting Of Movies List ******")
        self.mlp.sort_movie_list_by('Release Date')
        list_sorted_movies = self.mlp.get_top_n_movie_list()
        self.list_actual_movies_details.sort(key=lambda x: x['Release Date'], reverse=True)
        list_actual_movies = [movDict['Movie Name'] for movDict in self.list_actual_movies_details]
        if list_actual_movies == list_sorted_movies:
            assert True
            self.logger.info("******  Verifying Sorting Of Movies List by Release Date is passed ******")
        else:
            self.mlp.save_screenshot("test_sortingOfMoviesListByReleaseDate")
            self.logger.info("******  Verifying Sorting Of Movies List by Release Date is failed ******")
            assert False

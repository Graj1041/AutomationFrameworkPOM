from utilities.locators import *
from pageObjects.BasePage import BasePage
from utilities.commonUtility import commonUtility

class MovieListPage(BasePage):
    """Top 250 Movie List Page of imdb.com"""

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MovieListPageLocators
        self.comm_util = commonUtility()

    def get_top_n_movie_list(self, n=250):
        l_movie_name = []
        if self.is_visible(self.locators.HDR_RECENT_MOVIES):
            movie_name_elements = self.get_element_list(self.locators.LNK_MOVIES_NAME)
            for i in range(n):
                l_movie_name.append(movie_name_elements[i].text)
        return l_movie_name

    def change_order_of_movie_list(self):
        self.click(self.locators.BTN_REVERSE_ORDER)

    def sort_movie_list_by(self, value):
        options_list = self.get_drop_down_list_options(self.locators.DRP_SORT_BY)
        for option in options_list:
            if option.text.strip() == value:
                option.click()
                break

    def get_top_250_movies_list(self, n=250):
        l_top_250_movie = []
        if self.is_visible(self.locators.HDR_RECENT_MOVIES):
            movie_name_elements = self.get_element_list(self.locators.LNK_MOVIES_NAME)
            movie_rating_elements = self.get_element_list(self.locators.MOVIES_RATING)
            movie_year_elements = self.get_element_list(self.locators.MOVIES_YEAR)

            for i in range(n):
                l_top_250_movie.append(movie_name_elements[i].text + ' ===> ' + movie_rating_elements[i].text + ' ===> ' + movie_year_elements[i].text)

        movie_data = '\n'.join(l_top_250_movie)
        self.comm_util.save_data('ResultMovies.txt', movie_data)

    def save_movie_list(self, fileName, movie_list):
        all_movies = '\n'.join(movie_list)
        with open('.\\Reports\\' + fileName + '.txt', "w") as movie_file:
            movie_file.write(all_movies)

    def get_details_of_movies(self,n=250):
        if self.is_visible(self.locators.HDR_RECENT_MOVIES):
            movie_name_elements = self.get_element_list(self.locators.LNK_MOVIES_NAME)
            movie_rating_elements = self.get_element_list(self.locators.MOVIES_RATING)
            movie_year_elements = self.get_element_list(self.locators.MOVIES_YEAR)
            movie_rating_count_elements = self.get_element_list(self.locators.MOVIES_RATING_COUNT)
            list_movies_details = []
            for i in range(n):
                dict_movie_details = {}
                dict_movie_details['Movie Name'] = movie_name_elements[i].text
                dict_movie_details['Number of Ratings'] = int((movie_rating_count_elements[i].get_attribute('title')).split(' ')[3].replace(',',''))
                dict_movie_details['IMDb Rating'] = float(movie_rating_elements[i].text)
                dict_movie_details['Release Date'] = int(movie_year_elements[i].text.strip('()'))
                list_movies_details.append(dict_movie_details)
        self.comm_util.save_data('ResultMoviesDetails.txt', str(list_movies_details))
        return list_movies_details


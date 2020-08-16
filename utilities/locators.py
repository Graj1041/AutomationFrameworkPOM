from selenium.webdriver.common.by import By


class HomePageLocators():

    BTN_MENU = (By.XPATH, "//*[@id='imdbHeader-navDrawerOpen--desktop']/div")
    LNK_TOP_RATED_MOVIES = (By.XPATH, "//*[@id='imdbHeader']/div[2]/aside/div/div[2]/div/div[1]/span/div/div/ul/a[3]")


class MovieListPageLocators():
    LNK_MOVIES_NAME = (By.XPATH, '//table[@class="chart full-width"]//td[@class="titleColumn"]/a')
    MOVIES_RATING = (By.CLASS_NAME, r'imdbRating')
    MOVIES_YEAR = (By.CSS_SELECTOR, 'span.secondaryInfo')
    MOVIES_RATING_COUNT = (By.CSS_SELECTOR, 'strong')
    DRP_SORT_BY = (By.ID, 'lister-sort-by-options')
    BTN_REVERSE_ORDER = (By.XPATH, '//*[@id="main"]/div/span/div/div/div[3]/div/div/div[1]/span')
    HDR_RECENT_MOVIES = (By.XPATH, '//*[@id="rvi-div"]/div/div[1]/h3')

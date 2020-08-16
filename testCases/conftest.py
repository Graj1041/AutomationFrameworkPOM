from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
import pytest


@pytest.fixture()
def setupDriver(browser):
    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.headless = False
        options.add_experimental_option('useAutomationExtension', False)
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options = options)
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:   # default browser
        driver = webdriver.Ie(executable_path=IEDriverManager().install())
    return driver


''' For cross browser testing '''
def pytest_addoption(parser):   # This will get the value from CLI
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


######### For Generating HTML Reports #######

# It is hook for adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'IMDB'
    config._metadata['Module Name'] = 'IMDB Top 250 Movies'
    config._metadata['Tester'] = 'Raj'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


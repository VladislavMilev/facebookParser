import pytest
from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def driver_manager():

    driver: WebDriver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.implicitly_wait(2)
    driver.set_window_size(1500, 1000)
    yield driver
    driver.quit()
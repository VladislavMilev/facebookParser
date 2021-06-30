from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class SearchEngine:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def find_element(self, locator, time=2):
        try:
            return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator),
                                                          message=f"Локатор '{locator}' не найден!")
        except Exception as error:
            pass

    def find_elements(self, locator, time=2):
        return WebDriverWait(self.driver, time).until(ec.presence_of_all_elements_located(locator),
                                                      message=f"Локатор '{locator}' не найден!")

    def go_to_search_engine(self):
        return self.driver.get(self.url)
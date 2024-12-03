from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TrainListPage():

    def __init__(self, driver):
        self.driver = driver
        self.driver_explicit_wait = WebDriverWait(self.driver, 20)

    # Element Locators

    results_header = (By.XPATH, "//div[@class='tbis-div']//span")


    def get_results_head(self):
        return self.driver_explicit_wait.until(EC.visibility_of_element_located(self.results_header)).text
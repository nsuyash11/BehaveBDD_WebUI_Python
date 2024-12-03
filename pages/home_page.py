from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from pages.registration_page import RegistrationPage
from pages.pnr_page import PNRPage

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver_explicit_wait = WebDriverWait(self.driver, 20)

    # Element Locators
    search_button = (By.XPATH, "//button[@type='submit' and text()='Search']")

    register_link = (
        By.XPATH,
        "//a[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), ' register ')]",
    )

    from_textbox = (
        By.XPATH,
        "//input[@class='ng-tns-c57-8 ui-inputtext ui-widget ui-state-default ui-corner-all ui-autocomplete-input ng-star-inserted']",
    )
    # from_textbox = (By.CSS_SELECTOR, ".ng-tns-c57-8")

    to_textbox = (
        By.XPATH,
        "//input[@class='ng-tns-c57-9 ui-inputtext ui-widget ui-state-default ui-corner-all ui-autocomplete-input ng-star-inserted']",
    )

    date_textbox = (
        By.XPATH,
        "//input[@class='ng-tns-c58-10 ui-inputtext ui-widget ui-state-default ui-corner-all ng-star-inserted']",
    )

    quota_div = (
        By.XPATH,
        "//div[@class='ng-tns-c65-12 ui-dropdown ui-widget ui-state-default ui-corner-all']",
    )

    quota_list_items = (
        By.XPATH,
        "//p-dropdownitem[@class='ng-tns-c65-12 ng-star-inserted']",
    )

    travel_class_div = (
        By.XPATH,
        "//div[@class='ng-tns-c65-11 ui-dropdown ui-widget ui-state-default ui-corner-all']",
    )

    travel_class_list_items = (
        By.XPATH,
        "//p-dropdownitem[@class='ng-tns-c65-11 ng-star-inserted']",
    )

    just_page_div = (By.XPATH, "//div[@class='col-xs-12 loginhead hidden-xs']")

    toast_error_summary = (By.XPATH, "//div[contains(@class, 'ui-toast-summary')]")
    toast_error_detail = (By.XPATH, "//div[contains(@class, 'ui-toast-detail')]")

    confirmation_box_yes = (
        By.XPATH,
        "//button[@type='button' and contains(@class, 'ng-tns-c56-7')]",
    )

    pnr_link = (By.XPATH, "//a/label[text()='PNR STATUS']")

    # register_page
    username_textbox = (By.ID, "userName")

    def load_home_page(self):
        self.driver.get("https://www.irctc.co.in/nget/train-search")
        checkloaded = self.driver_explicit_wait.until(
            EC.element_to_be_clickable(self.search_button)
        )
        print("Loaded Home tab from link : ", self.driver.current_window_handle)
        return self

    def load_registration_page_toplink(self):
        register_link_el = self.driver_explicit_wait.until(
            EC.element_to_be_clickable(self.register_link)
        )
        register_link_el.click()

        reg_page = RegistrationPage(self.driver).wait_for_full_load()
        return reg_page

    def load_registration_page_directurl(self):
        self.driver.get("https://www.irctc.co.in/nget/profile/user-signup")

        reg_page = RegistrationPage(self.driver).wait_for_full_load()
        self.click_on_page()

        return reg_page

    def enter_from_station(self, from_station):
        tbox = self.driver_explicit_wait.until(
            EC.element_to_be_clickable(self.from_textbox)
        )
        tbox.clear()
        tbox.send_keys(from_station)

        self.click_on_page()

    def enter_to_station(self, to_station):
        tbox = self.driver_explicit_wait.until(
            EC.element_to_be_clickable(self.to_textbox)
        )
        tbox.clear()
        tbox.send_keys(to_station)

        self.click_on_page()

    def enter_date(self, jdate):
        tbox = self.driver_explicit_wait.until(
            EC.element_to_be_clickable(self.date_textbox)
        )

        tbox.send_keys(Keys.CONTROL + "a")
        tbox.send_keys(Keys.BACKSPACE)

        tbox.send_keys(jdate)

        self.click_on_page()

    def click_search(self):
        self.driver_explicit_wait.until(
            EC.element_to_be_clickable(self.search_button)
        ).click()

    def select_quota(self, quota):
        self.driver_explicit_wait.until(
            EC.element_to_be_clickable(self.quota_div)
        ).click()
        quota_list_items = self.driver.find_elements(*self.quota_list_items)

        wanted_quota_item = 0
        for item in quota_list_items:
            quota_text = item.find_element(By.XPATH, ".//li/span").text
            if quota.lower() in quota_text.lower():
                wanted_quota_item = item

        wanted_quota_item.click()

        self.click_on_page()

    def select_travel_class(self, travel_class):
        self.driver_explicit_wait.until(
            EC.element_to_be_clickable(self.travel_class_div)
        ).click()
        travel_class_list_items = self.driver.find_elements(
            *self.travel_class_list_items
        )

        wanted_travel_class_item = 0
        for item in travel_class_list_items:
            travel_class_text = item.find_element(By.XPATH, ".//li/span").text
            if travel_class.lower() in travel_class_text.lower():
                wanted_travel_class_item = item

        wanted_travel_class_item.click()

        self.click_on_page()

    def click_on_page(self):
        self.driver.find_element(*self.just_page_div).click()

    def check_error_message(self):
        error_text = self.driver_explicit_wait.until(
            EC.visibility_of_element_located(self.toast_error_detail)
        ).text
        return error_text

    def click_confirm_yes(self):
        confirm_box_yes = self.driver_explicit_wait.until(
            EC.visibility_of_element_located(self.confirmation_box_yes)
        )
        confirm_box_yes.click()

    def check_pnr_status(self):
        previous_tabs = set(self.driver.window_handles)

        self.driver_explicit_wait.until(
            EC.element_to_be_clickable(self.pnr_link)
        ).click()
        
        now_tabs = set(self.driver.window_handles)
        new_tab = now_tabs.difference(previous_tabs).pop()
        print("Switching focus to pnr tab : ", new_tab)

        # change driver focus to this new opened tab 
        self.driver.switch_to.window(new_tab)
        
        pnr_page = PNRPage(self.driver)
        pnr_page.wait_for_full_load()

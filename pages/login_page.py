from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
from pages.registration_page import RegistrationPage
from utils.read_captcha import get_captcha_imgtostr


class LoginPage:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.driver_explicit_wait = WebDriverWait(self.driver, 20)

    # Element Locators
    login_link = (By.XPATH, '//a[@class="search_btn loginText ng-star-inserted"]')
    username_input = (By.XPATH, '//input[@formcontrolname="userid"]')
    password_input = (By.XPATH, '//input[@formcontrolname="password"]')
    captcha_input = (By.XPATH, '//input[@id="captcha"]')
    signin_button = (
        By.XPATH,
        "//button[@type='submit' and contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'),'sign in')]",
    )
    forgot_details_link = (
        By.XPATH,
        "//strong[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'),'forgot')]",
    )
    register_button = (
        By.XPATH,
        "//label[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'),'register')]",
    )
    captcha_image = (By.XPATH, '//img[@class="captcha-img"]')
    login_error = (By.XPATH, '//div[@class="loginError"]')

    forgot_page_header = (By.XPATH, "//div[@class='bth_header heading-font row text-center']")
    register_page_header = (By.XPATH, "//strong[normalize-space()='Create Your IRCTC account']")


    # Element Actions
    def load_login(self):
        login_button = self.driver_explicit_wait.until(EC.visibility_of_element_located(self.login_link))
        login_button.click()

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def enter_captcha(self, captcha):
        self.driver.find_element(*self.captcha_input).send_keys(captcha)

    def click_sign_in(self):
        self.driver.find_element(*self.signin_button).click()

    def click_forgot_details(self):
        forgot_link = self.driver_explicit_wait.until(EC.element_to_be_clickable(self.forgot_details_link))
        forgot_link.click()

    def load_registration_page(self):
        self.driver.find_element(*self.register_button).click()
        return RegistrationPage(self.driver).wait_for_full_load()

    def get_login_error(self):
        error_msgbox = self.driver_explicit_wait.until(EC.visibility_of_element_located(self.login_error))
        return error_msgbox.text

    def capture_captcha_screenshot(self):
        captcha_image_element = self.driver_explicit_wait.until(EC.visibility_of_element_located(self.captcha_image))
        captcha_image_element.screenshot("./screenshots/login/captcha_img.png")

    def get_captcha(self):
        return get_captcha_imgtostr("./screenshots/login/captcha_img.png")
    
    def get_forgot_page_header(self):
        forgot_page_header = self.driver_explicit_wait.until(EC.visibility_of_element_located(self.forgot_page_header)).text
        return forgot_page_header
    
    def get_register_page_header(self):
        register_page_header = self.driver_explicit_wait.until(EC.visibility_of_element_located(self.register_page_header)).text
        return register_page_header
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from utils.read_captcha import get_captcha_imgtostr


class PNRPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver_explicit_wait = WebDriverWait(self.driver, 20)

    # Element Locators
    pnr_textbox = (By.XPATH, "//input[@id='inputPnrNo']")

    pnr_submit_button = (By.XPATH, "//input[@id='modal1' and @value='Submit']")

    captcha_img = (By.XPATH, "//img[@id='CaptchaImgID']")
    captcha_textbox = (By.XPATH, "//input[@id='inputCaptcha']")
    captcha_submit_button = (By.XPATH, "//input[@id='submitPnrNo' and @value='Submit']")

    error_message = (By.XPATH, "//p[@id='errorMessage']")
    captcha_error_message = (By.XPATH, "//p[@id='errorMessagemodal']")

    pnr_details_table = (By.XPATH, "//table[@id='psgnDetailsTable']")


    # Element/Page Actions

    def wait_for_full_load(self):
        checkloaded = self.driver_explicit_wait.until(
            EC.element_to_be_clickable(self.pnr_textbox)
        )

    def enter_pnr(self, pnr):
        self.driver_explicit_wait.until(
            EC.element_to_be_clickable(self.pnr_textbox)
        ).send_keys(pnr)

    def submit_pnr(self):
        self.driver_explicit_wait.until(
            EC.element_to_be_clickable(self.pnr_submit_button)
        ).click()

    def capture_captcha_screenshot(self):
        captcha_img = self.driver_explicit_wait.until(
            EC.visibility_of_element_located(self.captcha_img)
        )
        captcha_img.screenshot("./screenshots/pnr/captcha_img.png")

    def get_captcha_text(self):
        captcha_text = get_captcha_imgtostr("./screenshots/pnr/captcha_img.png")
        captcha_text_trimmed = ""
        captcha_operation = ""
        for char in captcha_text:
            if char != " " and char != "=" and char !="?":
                captcha_text_trimmed += char
            if char == "+":
                captcha_operation = "+"
            if char == "-":
                captcha_operation = "-"
        print("from page : ", captcha_text, "trimmed :", captcha_text_trimmed)

        captcha_words_list = captcha_text_trimmed.split(captcha_operation)
        print("from page : ", captcha_words_list)
        
        if captcha_operation == "+":
            value = int(captcha_words_list[0]) + int(captcha_words_list[1])
        if captcha_operation == "-":
            value = int(captcha_words_list[0]) - int(captcha_words_list[1])

        return str(value)

    def enter_captcha(self, captcha):
        self.driver_explicit_wait.until(
            EC.visibility_of_element_located(self.captcha_textbox)
        ).send_keys(captcha)

    def submit_captcha(self):
        self.driver_explicit_wait.until(
            EC.element_to_be_clickable(self.captcha_submit_button)
        ).click()

    def get_error_message(self):
        return self.driver_explicit_wait.until(EC.visibility_of_element_located(self.error_message)).text
    
    def get_captcha_error_message(self):
        return self.driver_explicit_wait.until(EC.visibility_of_element_located(self.captcha_error_message)).text

    def check_pnr_details_table_presence(self):
        try:
            checkloaded = self.driver_explicit_wait.until(EC.visibility_of_element_located(self.pnr_details_table))
            return True
        except Exception:
            return False
        
    def close_tab(self):
        print("Closing current focus tab : ", self.driver.current_window_handle)
        self.driver.close()
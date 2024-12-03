from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.read_captcha import get_captcha_imgtostr


class RegistrationPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver_explicit_wait = WebDriverWait(self.driver, 20)

    # Element Locators
    register_link = (
        By.XPATH,
        "//a[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), ' register ')]",
    )

    username_textbox = (By.ID, "userName")
    fullname_textbox = (By.ID, "fullName")
    password_textbox = (By.ID, "usrPwd")
    cnfpwd_textbox = (By.ID, "cnfUsrPwd")
    email_textbox = (By.ID, "email")
    mobile_code_dropdown = (
        By.XPATH,
        "//select[@type='text' and @class='form-control']",
    )
    mobile_textbox = (By.ID, "mobile")
    captcha_image = (By.XPATH, "//img[@class='captcha-img']")
    captcha_textbox = (By.ID, "captcha")
    submit_button = (By.XPATH, "//button[@type='submit']")

    sign_in_link = (
        By.XPATH,
        "//*[contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'sign in')]",
    )

    username_validation_error = (
        By.XPATH,
        "//span[not(@hidden) and contains(text(), 'User Name')]",
    )

    fullname_validation_error = (
        By.XPATH,
        "//span[not(@hidden) and contains(text(), 'Full Name')]",
    )

    password_validation_error = (
        By.XPATH,
        "//span[not(@hidden) and contains(text(), 'Password')]",
    )

    confirm_password_validation_error = (
        By.XPATH,
        "//span[not(@hidden) and contains(text(), 'Confirm')]",
    )

    email_validation_error = (
        By.XPATH,
        "//span[not(@hidden) and contains(text(), 'Email')]",
    )

    mobile_validation_error = (
        By.XPATH,
        "//span[not(@hidden) and contains(text(), 'Mobile No')]",
    )

    captcha_validation_error = (
        By.XPATH,
        "//span[not(@hidden) and contains(text(), 'Captcha is')]",
    )

    register_page_header = (By.XPATH, "//strong[normalize-space()='Create Your IRCTC account']")

    
    # need to load this from home page driver
    def load_register_page(self):
        register_link_el = self.driver_explicit_wait.until(EC.element_to_be_clickable(self.register_link))
        register_link_el.click()
        checkloaded = self.driver_explicit_wait.until(EC.visibility_of_element_located(self.username_textbox))
        return self
    
    def wait_for_full_load(self):
        checkloaded = self.driver_explicit_wait.until(EC.visibility_of_element_located(self.username_textbox))
        return self

    def enter_username(self, username):
        self.driver_explicit_wait.until(EC.visibility_of_element_located(self.username_textbox)).send_keys(username)

    def enter_fullname(self, fullname):
        self.driver.find_element(*self.fullname_textbox).send_keys(fullname)

    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def enter_cnfpwd(self, cnfpwd):
        self.driver.find_element(*self.cnfpwd_textbox).send_keys(cnfpwd)

    def enter_email(self, email):
        self.driver.find_element(*self.email_textbox).send_keys(email)

    def enter_mobile(self, mobile):
        self.driver.find_element(*self.mobile_textbox).send_keys(mobile)

    def capture_captcha_screenshot(self):
        captcha_image_element = self.driver_explicit_wait.until(EC.visibility_of_element_located(self.captcha_image))
        captcha_image_element.screenshot("./screenshots/registration/captcha_img.png")

    def get_captcha(self):
        return get_captcha_imgtostr("./screenshots/registration/captcha_img.png")

    def enter_captcha(self, captcha):
        self.driver.find_element(*self.captcha_textbox).send_keys(captcha)

    def click_submit(self):
        self.driver.find_element(*self.submit_button).click()

    def click_sign_in(self):
        self.driver.find_element(*self.sign_in_link).click()

    def get_username_validation(self):
        msgbox = self.driver_explicit_wait.until(
            EC.visibility_of_element_located(self.username_validation_error)
        )
        msg = msgbox.text
        return msg
    
    def get_fullname_validation(self):
        msgbox = self.driver_explicit_wait.until(
            EC.visibility_of_element_located(self.fullname_validation_error)
        )
        msg = msgbox.text
        return msg
    
    def get_password_validation(self):
        msgbox = self.driver_explicit_wait.until(
            EC.visibility_of_element_located(self.password_validation_error)
        )
        msg = msgbox.text
        return msg
    
    def get_cnf_pwd_validation(self):
        msgbox = self.driver_explicit_wait.until(
            EC.visibility_of_element_located(self.confirm_password_validation_error)
        )
        msg = msgbox.text
        return msg

    def get_email_validation(self):
        msgbox = self.driver_explicit_wait.until(
            EC.visibility_of_element_located(self.email_validation_error)
        )
        msg = msgbox.text
        return msg
    
    def get_mobile_validation(self):
        msgbox = self.driver_explicit_wait.until(
            EC.visibility_of_element_located(self.mobile_validation_error)
        )
        msg = msgbox.text
        return msg

    def get_captcha_validation(self):
        msgbox = self.driver_explicit_wait.until(
            EC.visibility_of_element_located(self.captcha_validation_error)
        )
        msg = msgbox.text
        return msg
    
    def get_page_title(self):
        title = self.driver_explicit_wait.until(EC.visibility_of_element_located(self.register_page_header)).text
        return title
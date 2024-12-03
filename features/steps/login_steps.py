import time
from behave import given, when, then
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage


@given("User is on Login Page")
def step_impl(context):
    context.driver.get("https://www.irctc.co.in/nget/train-search")

    # not store anything from here, just to use method written there to load page
    LoginPage(context.driver).load_login()

    # pass this state of driver ie Loaded login page to LoginPage class and store this LoginPage object in context.login_page variable to re-use it further for tests repeatedly
    context.login_page = LoginPage(context.driver)


@when("User enters valid credentials in '{username}', '{password}', captcha")
def step_impl(context, username, password):
    context.login_page.enter_username(username)
    context.login_page.enter_password(password)

    context.login_page.capture_captcha_screenshot()
    captcha_text = context.login_page.get_captcha()
    context.login_logger.debug(f"captcha_text : {captcha_text}")
    context.login_page.enter_captcha(captcha_text)


@when("User clicks Sign In button")
def step_impl(context):
    context.login_page.click_sign_in()
    time.sleep(2)


@then("User should be able to log in successfully")
def load_login_page(context):
    actual_page_title = context.driver.title.lower()
    expected_page_title = "Welcome".lower()

    assert expected_page_title in actual_page_title, "Successful Login Page title error"


@when("User enters invalid '{username}', valid '{password}', valid captcha")
def enter_invalid_un_valid_pwd_cap(context, username, password):
    if username == "empty":
        username = ""
    if username == "space":
        username = "     "

    context.login_page.enter_username(username)
    context.login_page.enter_password(password)

    context.login_page.capture_captcha_screenshot()
    captcha_text = context.login_page.get_captcha()
    context.login_logger.debug(f"captcha_text : {captcha_text}")
    context.login_page.enter_captcha(captcha_text)


@then("User should get proper warning error '{message}' for login User")
def assert_user_warning(context, message):
    actual_login_error = context.login_page.get_login_error().lower()
    expected_login_error = message.lower()

    context.login_logger.debug(f"actual error msg : {actual_login_error}")
    context.login_logger.debug(f"expected error msg : {expected_login_error}")

    assert (
        expected_login_error in actual_login_error
    ), "Invalid User Login Error Message problem"


@when("User enters valid '{username}', invalid '{password}', valid captcha")
def enter_valid_un_cap_invalid_pwd(context, username, password):
    if password == "empty":
        password = ""
    if password == "space":
        password = "     "

    context.login_page.enter_username(username)
    context.login_page.enter_password(password)

    context.login_page.capture_captcha_screenshot()
    captcha_text = context.login_page.get_captcha()
    context.login_logger.debug(f"captcha_text : {captcha_text}")
    context.login_page.enter_captcha(captcha_text)


@then("User should get proper warning error '{message}' for login Password")
def assert_password_warning(context, message):
    actual_password_error = context.login_page.get_login_error().lower()
    expected_password_error = message.lower()

    context.login_logger.debug(f"actual error msg : {actual_password_error}")
    context.login_logger.debug(f"expected error msg : {expected_password_error}")

    assert (
        expected_password_error in actual_password_error
    ), "Invalid Password Login Error Message problem"


@when(
    'User enters valid "{username}", valid matching "{password}", invalid "{captcha}"'
)
def enter_valid_un_pwd_invalid_captcha(context, username, password, captcha):
    if captcha == "empty":
        captcha = ""
    if captcha == "space":
        captcha = "     "

    context.login_page.enter_username(username)
    context.login_page.enter_password(password)
    context.login_page.enter_captcha(captcha)


@when("User keeps username, password, captcha fields blank")
def enter_blank_fields(context):
    context.login_page.enter_username("")
    context.login_page.enter_password("")
    context.login_page.enter_captcha("")


@then('User should get proper warning error "{message}" for login captcha')
def assert_captcha_warning(context, message):
    actual_captcha_error = context.login_page.get_login_error().lower()
    expected_captcha_error = message.lower()

    context.login_logger.debug(f"actual error msg : {actual_captcha_error}")
    context.login_logger.debug(f"expected error msg : {expected_captcha_error}")

    assert (
        expected_captcha_error in actual_captcha_error
    ), "Invalid Captcha Login Error Message problem"


@then("User should get proper warning error message for all blank entries")
def assert_blanks_warning(context):
    actual_captcha_error = context.login_page.get_login_error().lower()
    expected_captcha_error = "Please Enter Valid User ID".lower()

    context.login_logger.debug(f"actual error msg : {actual_captcha_error}")
    context.login_logger.debug(f"expected error msg : {expected_captcha_error}")

    assert (
        expected_captcha_error in actual_captcha_error
    ), "Invalid Captcha Login Error Message problem"


@when("User clicks Forgot Account Details link")
def click_forgot_link(context):
    context.login_page.click_forgot_details()


@then("User should be directed to Forgot Account Details Page")
def step_impl(context):

    actual_page_title = context.login_page.get_forgot_page_header().lower()
    expected_page_title = "FORGOT ACCOUNT DETAILS".lower()

    context.login_logger.debug(f"actual forgot page title : {actual_page_title}")

    assert (
        expected_page_title in actual_page_title
    ), "Forgot Account Details Page title problem"


@when("User clicks Register button")
def step_impl(context):
    context.login_page.load_registration_page()


@then("User should be directed to Account Registration Page")
def step_impl(context):

    actual_page_title = context.login_page.get_register_page_header().lower()
    expected_page_title = "Create Your IRCTC account".lower()

    context.login_logger.debug(f"Actual register page title : {actual_page_title}")
    context.registration_logger.debug(f"Actual register page title : {actual_page_title}")

    assert expected_page_title in actual_page_title, "Create Your IRCTC account"

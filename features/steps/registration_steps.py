import time
from behave import given, when, then

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from utils.read_captcha import get_captcha_imgtostr


@given(u'User is on Registration Page')
def load_registration_page(context):
    if "no-background" not in context.tags:
        # driver will load home page and return HomePage object (we are not storing it in variable)
        context.home_page = HomePage(context.driver).load_home_page()
        
        # same driver will load reg page and create RegPage class object and store in a variable for further tests reuse
        # context.registration_page = RegistrationPage(context.driver).load_register_page()
        context.registration_page = context.home_page.load_registration_page()

        context.registration_logger.debug("Loaded Reg Page")

@when(u'User clicks Submit button')
def click_submit(context):
    context.registration_page.click_submit()

# ===== ALL BLANK

@when(u'User enters all fields blank')
def enter_all_fields_blank(context):
    context.registration_page.enter_username("")
    context.registration_page.enter_fullname("")
    context.registration_page.enter_password("")
    context.registration_page.enter_cnfpwd("")
    context.registration_page.enter_email("")
    context.registration_page.enter_mobile("")
    context.registration_page.enter_captcha("")


@then(u'User should get appropriate warning message on all fields')
def test_all_blank_validations(context):
    actual_username_warning = context.registration_page.get_username_validation().lower()
    actual_fullname_warning = context.registration_page.get_fullname_validation().lower()
    actual_password_warning = context.registration_page.get_password_validation().lower()
    actual_cnfpwd_warning = context.registration_page.get_cnf_pwd_validation().lower()
    actual_email_warning = context.registration_page.get_email_validation().lower()
    actual_mobile_warning = context.registration_page.get_mobile_validation().lower()
    actual_captcha_warning = context.registration_page.get_captcha_validation().lower()

    context.registration_logger.debug(f"actual validations :\n{actual_username_warning} \n{actual_fullname_warning} \n{actual_password_warning} \n{actual_cnfpwd_warning} \n{actual_email_warning} \n{actual_mobile_warning} \n{actual_captcha_warning}")

    expected_username_warning = "user"
    expected_fullname_warning = "full"
    expected_password_warning = "password"
    expected_cnfpwd_warning = "confirm"
    expected_email_warning = "email"
    expected_mobile_warning = "mobile"
    expected_captcha_warning = "captcha"


    assert expected_username_warning in actual_username_warning, "User Name validation problem"
    assert expected_fullname_warning in actual_fullname_warning, "Full Name validation problem"
    assert expected_password_warning in actual_password_warning, "Password validation problem"
    assert expected_cnfpwd_warning in actual_cnfpwd_warning, "Confirm Password validation problem"
    assert expected_email_warning in actual_email_warning, "Email validation problem"
    assert expected_mobile_warning in actual_mobile_warning, "Mobile validation problem"
    assert expected_captcha_warning in actual_captcha_warning, "Captcha validation problem"

# ===== USERNAME

@when('User enters invalid username "{username}" and other fields "{fullname}", "{password}", "{email}", "{mobile}" valid')
def enter_invalid_uname_valid_others(context, username, fullname, password, email, mobile):
    if username == "empty":
        username = ""
    if username == "space":
        username = "     "
    context.registration_page.enter_username(username)
    
    context.registration_page.enter_fullname(fullname)
    context.registration_page.enter_password(password)
    context.registration_page.enter_cnfpwd(password)
    context.registration_page.enter_email(email)
    context.registration_page.enter_mobile(mobile)
    
    context.registration_page.capture_captcha_screenshot()
    captcha_text = get_captcha_imgtostr("./screenshots/registration/captcha_img.png")
    context.registration_page.enter_captcha(captcha_text)

    context.registration_logger.debug(f"Entered values : {username, fullname, password, email, mobile, captcha_text}")


@then('User should get appropriate warning message "{message}" for username field')
def test_username_validation(context, message):
    actual_username_warning = context.registration_page.get_username_validation().lower()

    expected_username_warning = message.lower()

    context.registration_logger.debug(f"actual_username_warning : {actual_username_warning}")
    assert expected_username_warning in actual_username_warning, "Invalid Username validation problem"


# ===== FULL NAME

@when(u'User enters invalid fullname "{fullname}" and all other fields "{username}", "{password}", "{email}", "{mobile}" valid')
def enter_invalid_fullname_valid_others(context, username, fullname, password, email, mobile):
    if fullname == "empty":
        fullname = ""
    if fullname == "space":
        fullname = "     "
    context.registration_page.enter_fullname(fullname)

    context.registration_page.enter_username(username)
    context.registration_page.enter_password(password)
    context.registration_page.enter_cnfpwd(password)
    context.registration_page.enter_email(email)
    context.registration_page.enter_mobile(mobile)
    
    context.registration_page.capture_captcha_screenshot()
    captcha_text = get_captcha_imgtostr("./screenshots/registration/captcha_img.png")
    context.registration_page.enter_captcha(captcha_text)

    context.registration_logger.debug(f"Entered values : {username, fullname, password, email, mobile, captcha_text}")

@then(u'User should get appropriate warning "{message}" for invalid fullname field')
def test_fullname_validation(context, message):
    actual_fullname_warning = context.registration_page.get_fullname_validation().lower()
    expected_fullname_warning = message.lower()
    context.registration_logger.debug(f"actual_username_warning : {actual_fullname_warning}")
    
    assert expected_fullname_warning in actual_fullname_warning, "Invalid Fullname validation problem"


# ===== PASSWORD

@when(u'User enters invalid password "{password}" and all other fields "{username}", "{fullname}", "{email}", "{mobile}" valid')
def enter_invalid_password_valid_others(context, username, fullname, password, email, mobile):
    if password == "empty":
        password = ""
    if password == "space":
        password = "     "
    context.registration_page.enter_password(password)

    context.registration_page.enter_username(username)
    context.registration_page.enter_fullname(fullname)
    context.registration_page.enter_cnfpwd(password)
    context.registration_page.enter_email(email)
    context.registration_page.enter_mobile(mobile)
    
    context.registration_page.capture_captcha_screenshot()
    captcha_text = get_captcha_imgtostr("./screenshots/registration/captcha_img.png")
    context.registration_page.enter_captcha(captcha_text)

    context.registration_logger.debug(f"Entered values : {username, fullname, password, email, mobile, captcha_text}")

@then(u'User should get appropriate warning "{message}" for invalid password field')
def test_password_validation(context, message):
    actual_password_warning = context.registration_page.get_password_validation().lower()
    expected_password_warning = message.lower()

    context.registration_logger.debug(f"actual_username_warning : {actual_password_warning}")

    assert expected_password_warning in actual_password_warning, "Invalid Password problem"

# ====== CNF PASSWORD

@when(u'User enters invalid confirm password "{cnfpwd}" and all other fields "{username}", "{fullname}", "{password}", "{email}", "{mobile}" valid')
def enter_invalid_cnfpwd_valid_others(context, username, cnfpwd, fullname, password, email, mobile):
    if cnfpwd == "empty":
        cnfpwd = ""
    if cnfpwd == "space":
        cnfpwd = "     "
    context.registration_page.enter_cnfpwd(password)

    context.registration_page.enter_username(username)
    context.registration_page.enter_fullname(fullname)
    context.registration_page.enter_password(password)
    context.registration_page.enter_email(email)
    context.registration_page.enter_mobile(mobile)
    
    context.registration_page.capture_captcha_screenshot()
    captcha_text = get_captcha_imgtostr("./screenshots/registration/captcha_img.png")
    context.registration_page.enter_captcha(captcha_text)

    context.registration_logger.debug(f"Entered values : {username, fullname, password, cnfpwd, email, mobile, captcha_text}")


@then(u'User should get appropriate warning "{message}" for invalid confirm password field')
def test_cnfpwd_validation(context, message):
    actual_cnfpwd_warning = context.registration_page.get_cnf_pwd_validation().lower()
    expected_cnfpwd_warning = message.lower()

    context.registration_logger.debug(f"actual_username_warning : {actual_cnfpwd_warning}")

    assert expected_cnfpwd_warning in actual_cnfpwd_warning, "Invalid Confirm Password validation problem"


# ===== EMAIL

@when(u'User enters invalid email "{email}" and all other fields "{username}", "{fullname}", "{password}", "{mobile}" valid')
def enter_invalid_email_valid_others(context, username, fullname, password, email, mobile):
    if email == "empty":
        email = ""
    if email == "space":
        email = "     "
    context.registration_page.enter_email(email)

    context.registration_page.enter_username(username)
    context.registration_page.enter_fullname(fullname)
    context.registration_page.enter_password(password)
    context.registration_page.enter_cnfpwd(password)
    context.registration_page.enter_mobile(mobile)
    
    context.registration_page.capture_captcha_screenshot()
    captcha_text = get_captcha_imgtostr("./screenshots/registration/captcha_img.png")
    context.registration_page.enter_captcha(captcha_text)

    context.registration_logger.debug(f"Entered values : {username, fullname, password, email, mobile, captcha_text}")


@then(u'User should get appropriate warning "{message}" for invalid email field')
def test_email_validation(context, message):
    actual_email_warning = context.registration_page.get_email_validation().lower()
    expected_email_warning = message.lower()

    context.registration_logger.debug(f"actual_username_warning : {actual_email_warning}")

    assert expected_email_warning in actual_email_warning, "Invalid Email validation problem"

# ===== MOBILE

@when(u'User enters invalid mobile "{mobile}" and all other fields "{username}", "{fullname}", "{password}", "{email}" valid')
def enter_invalid_mobile_valid_others(context, username, fullname, password, email, mobile):
    if mobile == "empty":
        mobile = ""
    if mobile == "space":
        mobile = "     "
    context.registration_page.enter_mobile(mobile)

    context.registration_page.enter_username(username)
    context.registration_page.enter_fullname(fullname)
    context.registration_page.enter_password(password)
    context.registration_page.enter_cnfpwd(password)
    context.registration_page.enter_email(email)
    
    context.registration_page.capture_captcha_screenshot()
    captcha_text = get_captcha_imgtostr("./screenshots/registration/captcha_img.png")
    context.registration_page.enter_captcha(captcha_text)

    context.registration_logger.debug(f"Entered values : {username, fullname, password, email, mobile, captcha_text}")


@then(u'User should get appropriate warning "{message}" for invalid mobile field')
def test_mobile_validation(context, message):
    actual_mobile_warning = context.registration_page.get_mobile_validation().lower()
    expected_mobile_warning = message.lower()

    context.registration_logger.debug(f"actual_username_warning : {actual_mobile_warning}")

    assert expected_mobile_warning in actual_mobile_warning, "Invalid Mobile No validation problem"

# ===== CAPTCHA

@when(u'User enters invalid captcha "{captcha}" and all other fields "{username}", "{fullname}", "{password}", "{email}", "{mobile}" valid')
def enter_invalid_captcha_valid_others(context, username, fullname, password, email, mobile, captcha):
    if captcha == "empty":
        captcha = ""
    if captcha == "space":
        captcha = "     "
    context.registration_page.enter_captcha(captcha)

    context.registration_page.enter_username(username)
    context.registration_page.enter_fullname(fullname)
    context.registration_page.enter_password(password)
    context.registration_page.enter_cnfpwd(password)
    context.registration_page.enter_email(email)
    context.registration_page.enter_mobile(mobile)

    context.registration_logger.debug(f"Entered values : {username, fullname, password, email, mobile, captcha}")


@then(u'User should get appropriate warning "{message}" for invalid captcha field')
def test_captcha_validation(context, message):
    actual_captcha_warning = context.registration_page.get_captcha_validation().lower()
    expected_captcha_warning = message.lower()

    context.registration_logger.debug(f"actual_username_warning : {actual_captcha_warning}")

    assert expected_captcha_warning in actual_captcha_warning, "Invalid Captcha validation problem"


# ===== ACCESS REGISTRATION PAGE

@given(u'User is on Home Page')
def load_home_page(context):
    context.home_page = HomePage(context.driver).load_home_page()

@when(u'User clicks Register link from links in top section')
def load_registration_page_from_toplink(context):    
    context.registration_page = context.home_page.load_registration_page_toplink()


@then(u'User should be able to load Registration Page')
def step_impl(context):
    actual_page_title = context.registration_page.get_page_title().lower()
    expected_page_title = "Create Your IRCTC account".lower()

    context.registration_logger.debug(f"Actual register page title : {actual_page_title}")

    assert (
        expected_page_title in actual_page_title
    ), "Forgot Account Details Page title problem"


@given(u'User is anywhere')
def step_impl(context):
    context.driver.get("https://google.co.in/")

@when(u'User hits direct Registration Page URL')
def load_registration_page_from_directurl(context):
    context.registration_page = context.home_page.load_registration_page_directurl()

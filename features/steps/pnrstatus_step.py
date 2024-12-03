from behave import given, when, then
from pages.home_page import HomePage
from pages.pnr_page import PNRPage

# hp = HomePage()
# pp = PNRPage()

# ===== FROM HOME PAGE TO PNR PAGE TRANSITIION

@when(u'User clicks PNR Status link')
def step_impl(context):
    # context will already contain home_page from previous GIVEN step 'User is on Home Page' implemented in another feature
    context.home_page.check_pnr_status()

@then(u'User should be able to load PNR Status Enquiry Page in separate tab')
def step_impl(context):
    context.pnr_page = PNRPage(context.driver)
    context.pnr_page.wait_for_full_load()

    context.pnr_page.close_tab()

# ===== PNR Page

@given(u'User is on PNR Page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.pnr_page = PNRPage(context.driver)

    context.home_page.load_home_page()
    context.home_page.check_pnr_status()
    context.pnr_page.wait_for_full_load()

@when(u'User enters PNR number "{pnr}"')
def step_impl(context, pnr):
    context.pnr_page.enter_pnr(pnr)

@when(u'User clicks Submit PNR button')
def step_impl(context):
    context.pnr_page.submit_pnr()

# ===== CAPTCHA ENTRY

@when(u'User enters valid captcha')
def step_impl(context):
    context.pnr_page.capture_captcha_screenshot()
    captcha_final_text = context.pnr_page.get_captcha_text()
    context.pnr_page.enter_captcha(captcha_final_text)

@when(u'User clicks Submit Captcha button')
def step_impl(context):
    context.pnr_page.submit_captcha()

@then(u'User should get warning message for PNR field validation')
def step_impl(context):
    actual_error_message = context.pnr_page.get_error_message().lower()
    context.pnrstatus_logger.debug(actual_error_message)

    assert "error" in actual_error_message, "Invalid PNR field validation Fail - Known Issue"

    context.pnr_page.close_tab()

# ===== INVALID PNR

@then('User should get warning "{message}" for invalid PNR')
def step_impl(context, message):
    actual_error_message = context.pnr_page.get_error_message().lower()
    expected_error_message = message.lower()

    context.pnrstatus_logger.debug(actual_error_message)

    assert expected_error_message in actual_error_message, "Some Problem in Non-existing PNR validation"

    context.pnr_page.close_tab()


# ===== INVALID CAPTCHA


@when(u'User enters invalid captcha')
def step_impl(context):
    context.pnr_page.enter_captcha("aB1@#")

@then(u'User should get warning "{message}" for invalid Captcha')
def step_impl(context, message):
    actual_error_message = context.pnr_page.get_captcha_error_message().lower()
    expected_error_message = message.lower()

    context.pnrstatus_logger.debug(actual_error_message)

    assert expected_error_message in actual_error_message, "Some Problem in Invalid Captcha validation"
    context.pnr_page.close_tab()


# ===== ALL VALID


@then(u'User should be able to see the PNR Status')
def step_impl(context):
    status_present = context.pnr_page.check_pnr_details_table_presence()

    assert status_present == True, "Some Problem in displaying PNR Details Table"

    context.pnr_page.close_tab()

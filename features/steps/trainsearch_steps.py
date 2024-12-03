from behave import given, when, then
from pages.home_page import HomePage
from pages.trainlist_page import TrainListPage

# hp = HomePage()
# tp = TrainListPage()

@when("User clicks Search button")
def click_search_step(context):
    context.home_page.click_search()


# ===== INVALID FROM/TO STATION


@when(
    'User enters invalid fromstation as "{fromstation}" and other fields "{tostation}", "{quota}", "{jdate}", "{travelclass}"'
)
def enter_invalid_fromstation_valid_others_step(context, fromstation, tostation, quota, jdate, travelclass):
    context.home_page = HomePage(context.driver)
    
    if fromstation == "empty":
        fromstation = ""
    if fromstation == "space":
        fromstation = "     "

    context.home_page.enter_from_station(fromstation)
    context.home_page.enter_to_station(tostation)
    context.home_page.select_quota(quota)
    context.home_page.enter_date(jdate)
    context.home_page.select_travel_class(travelclass)

    context.trainsearch_logger.debug(f"Entered values : {fromstation} {tostation} {quota} {jdate} {travelclass}")

@when(
    'User enters invalid tostation as "{tostation}" and other fields "{fromstation}", "{quota}", "{jdate}", "{travelclass}"'
)
def enter_invalid_tostation_valid_others_step(context, fromstation, tostation, quota, jdate, travelclass):
    if tostation == "empty":
        tostation = ""
    if tostation == "space":
        tostation = "     "

    context.home_page.enter_from_station(fromstation)
    context.home_page.enter_to_station(tostation)
    context.home_page.select_quota(quota)
    context.home_page.enter_date(jdate)
    context.home_page.select_travel_class(travelclass)

    context.trainsearch_logger.debug(f"Entered values : {tostation} {tostation} {quota} {jdate} {travelclass}")


@then('User should get appropriate warning error "{message}" for station input')
def assert_fromstation_validation_step(context, message):
    actual_error_msg = context.home_page.check_error_message()
    context.trainsearch_logger.debug(actual_error_msg)

    expected_error_msg = message

    assert expected_error_msg in actual_error_msg, "Problem in Error Toast Message"

# ===== INVALID DATE


@when(
    'User enters invalid date as "{jdate}" and other fields "{fromstation}", "{tostation}", "{quota}", "{travelclass}"'
)
def step_impl(context, fromstation, tostation, quota, jdate, travelclass):
    if jdate == "empty":
        jdate = ""
    if jdate == "space":
        jdate = "     "

    context.home_page.enter_from_station(fromstation)
    context.home_page.enter_to_station(tostation)
    context.home_page.select_quota(quota)
    context.home_page.enter_date(jdate)
    context.home_page.select_travel_class(travelclass)

    context.trainsearch_logger.debug(f"Entered values : {fromstation} {tostation} {quota} {jdate} {travelclass}")


@then('User should get appropriate warning error "{message}" for date input')
def step_impl(context, message):
    actual_error_msg = context.home_page.check_error_message()
    context.trainsearch_logger.debug(actual_error_msg)

    expected_error_msg = message

    assert expected_error_msg in actual_error_msg, "Problem in Error Toast Message"


# ===== NON-EXISTING ROUTE


@when(
    'User enters non-existing train route "{fromstation}" with "{tostation}" and other fields "{quota}", "{jdate}", "{travelclass}" valid'
)
def step_impl(context, fromstation, tostation, quota, jdate, travelclass):
    context.home_page.enter_from_station(fromstation)
    context.home_page.enter_to_station(tostation)
    context.home_page.select_quota(quota)
    context.home_page.enter_date(jdate)
    context.home_page.select_travel_class(travelclass)

    context.trainsearch_logger.debug(f"Entered values : {fromstation} {tostation} {quota} {jdate} {travelclass}")

@when('User confirms indirect journey search')
def step_impl(context):
    context.home_page.click_confirm_yes()

@then('User should get appropriate results "{message}" on train search list page')
def step_impl(context, message):
    context.trainlist_page = TrainListPage(context.driver)

    actual_result_msg = context.trainlist_page.get_results_head().lower()
    context.trainsearch_logger.debug(actual_result_msg)
    
    expected_result_msg = message.lower()

    assert expected_result_msg in actual_result_msg, "Problem in Result Header Message"


# ===== EXISTING ROUTE {travelclass} VALID


@when(
    'User enters existing train route "{fromstation}" with "{tostation}" and other fields "{quota}", "{jdate}", "{travelclass}" valid'
)
def step_impl(context, fromstation, tostation, quota, jdate, travelclass):
    context.home_page.enter_from_station(fromstation)
    context.home_page.enter_to_station(tostation)
    context.home_page.select_quota(quota)
    context.home_page.enter_date(jdate)
    context.home_page.select_travel_class(travelclass)

    context.trainsearch_logger.debug(f"Entered values : {fromstation} {tostation} {quota} {jdate} {travelclass}")


@then("User should get appropriate results on train search list page")
def step_impl(context):
    context.trainlist_page = TrainListPage(context.driver)

    actual_result_msg = context.trainlist_page.get_results_head().lower()
    context.trainsearch_logger.debug(actual_result_msg)
    
    actual_result_count = actual_result_msg.split()[0]

    assert int(actual_result_count) != 0, "Problem in Non-zero Results Header Count"
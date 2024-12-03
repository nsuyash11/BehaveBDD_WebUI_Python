from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import log_helper



# setup
def before_all(context):
    context.login_logger = log_helper.get_logger("setup_env-login_steps", "login_steps")
    context.registration_logger = log_helper.get_logger("setup_env-registration_steps", "registration_steps")
    context.trainsearch_logger = log_helper.get_logger("setup_env-trainsearch_steps", "trainsearch_steps")
    context.pnrstatus_logger = log_helper.get_logger("setup_env-pnrstatus_steps", "pnrstatus_steps")


# teardown
def after_all(context):

    # kill driver
    context.driver.quit()
    
    # remove loggers control on log files
    log_helper.remove_logfile_handler(context.login_logger)
    log_helper.remove_logfile_handler(context.registration_logger)
    log_helper.remove_logfile_handler(context.trainsearch_logger)
    log_helper.remove_logfile_handler(context.pnrstatus_logger)


# will execute before EACH EXAMPLE IN SCENARIOS / EACH SCENARIOS "SEPARATELY" even before backgorund steps
def before_scenario(context, scenario):
    if not hasattr(context, "driver"):
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-geolocation")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

        context.driver = webdriver.Chrome(chrome_options)
        context.driver.maximize_window()


def after_scenario(context, scenario):
    context.driver.quit() # Close the browser and end the session

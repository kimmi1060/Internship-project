from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options

from app.application import Application

def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    # driver_path = GeckoDriverManager().install()Tas
bs_user = 'kinjalpatel_OYWK3u'
bs_key = 'cequyzAGshrun9nyoz9f'
url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

options = Options()
bstack_options = {
"os": "Windows", #Windows, OS X
"osVersion": "10", #11, Sonoma
'browserName': 'chrome', #edge
'sessionName': scenario_name,
# }

    'deviceName': 'iphone 16 pro max',  # Replace with desired device
    'platformName': 'ios',  # Or Android'
    'browserName': 'Chrome',  # Mobile Chrome browser
    'sessionName': scenario_name,
}
options.set_capability('bstack:options)
context.driver = webdriver.Remote(command_executor=url, options=options)

# mobile_emulation = {"deviceName": "Samsung galaxy Z"}
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    # driver = webdriver.Remote(command_executor='http://155.0.0.1:4444/wd/hub',
    #                           desired_capabilities=chrome_options.to_capabilities())

    #
   # options = webdriver.ChromeOptions()
    # options.add_experimental_option("mobileEmulation", mobile_emulation)
    # Initialize WebDriver with mobile emulation
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(service=service, options=options)

context.driver.maximize_window()
context.driver.implicitly_wait(4)
context.driver.wait = WebDriverWait(context.driver, timeout=10)
context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)
    browser_init(context, scenario.name)

def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BasePage():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click_element(self, locator_type, locator_value):
        self.wait.until(EC.presence_of_element_located((locator_type, locator_value))).click()

    def enter_text(self, locator_type, locator_value, text):
        element = self.wait.until(EC.presence_of_element_located((locator_type, locator_value)))
        element.clear()
        element.send_keys(text)

    def move_to_element(self, locator_type, locator_value):
        action = ActionChains(self.driver)
        my_button = self.wait.until(EC.presence_of_element_located((locator_type, locator_value)))
        action.move_to_element(my_button).perform()

    def select_by_value(self, locator_type, locator_value, value):
        select = Select(self.driver.find_element(locator_type, locator_value))
        select.select_by_value(value)

    def force_click(self, locator_type, locator_value):
        element = self.driver.find_element(locator_type, value=locator_value)
        self.driver.execute_script("arguments[0].click();", element)

    def assert_input(self, locator_type, locator_value, name):
        element = self.driver.find_element(locator_type, value=locator_value)
        assert element.get_attribute("value") == name

    def send_photo(self, locator_type, locator_value, value):
        element = self.driver.find_element(locator_type, locator_value)
        element.send_keys(value)

    # def enable_element(self, locator_type, locator_value):
    #     disabled_element = self.driver.find_element(locator_type, value=locator_value)
    #     self.driver.execute_script("arguments[0].removeAttribute('disabled')", disabled_element)
    # def wait_for_appear_and_click(self, locator_type, locator_value):
    #     element = self.wait.until(EC.presence_of_element_located((locator_type, locator_value)))
    #     element.click()

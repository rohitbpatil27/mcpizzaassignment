from selenium.webdriver import Keys  # Import the Keys class for simulating keyboard keys
from selenium.webdriver.support.ui import WebDriverWait  # Import WebDriverWait for waiting for elements
from selenium.webdriver.support import expected_conditions as EC  # Import expected_conditions for defining conditions

class Selenium_Helper:
    """Helper class for common Selenium operations."""

    def __init__(self, driver):
        """Initialize Selenium_Helper with a WebDriver instance."""
        self.driver = driver

    def webelement_enter(self, locator, text):
        """Enter text into a web element identified by locator."""
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def webelement_click(self, locator):
        """Click on a web element identified by locator."""
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator)).click()

    def webelement_switchToiFrame(self, locator):
        """Switch to an iframe identified by locator."""
        WebDriverWait(self.driver, 5).until(EC.frame_to_be_available_and_switch_to_it(locator))

    def webelement_enterKey(self, locator):
        """Simulate pressing the Enter key on a web element identified by locator."""
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator)).send_keys(Keys.ENTER)

    def wait_for_element(self, locator):
        """Wait for a web element identified by locator to be visible."""
        try:
            element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
            return element
        except Exception as e:
            print(f"An error occurred while waiting for the element: {str(e)}")
            return None

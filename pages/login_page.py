from selenium.webdriver.common.by import By

from utils.helper import Selenium_Helper
from utils.locators import CommonLocators

# Base URL for the login page
baseURL = ("https://c0.avaamo.com/web_channels/cce5f713-c1f4-4666-8976-b091299cda81/demo.html?banner=true&demo=true"
           "&banner_text=%20&banner_title=This%20is%20how%20the%20chat%20agent%20shows%20up")

class LoginPage(Selenium_Helper):
    # Locators for elements on the login page
    button_chat = (By.XPATH, "//img[@alt='Chat agent button']")
    button_getStarted = (By.XPATH, "//a[normalize-space()='Get Started']")

    def __init__(self, driver):
        super().__init__(driver)

    def launchChatBot(self):
        """Launches the chatbot by clicking on the chat button and then the Get Started button."""
        self.webelement_click(self.button_chat)  # Clicks on the chat button
        self.webelement_click(self.button_getStarted)  # Clicks on the Get Started button
        # Switches to the iframe containing the chatbot
        self.webelement_switchToiFrame(CommonLocators.iframe_chatbot)

    def resetMessageBox(self):
        """Resets the message box by entering 'reset' and pressing Enter."""
        self.webelement_enter(CommonLocators.textarea_messagebox, "reset")  # Enters 'reset' in the message box
        self.webelement_enterKey(CommonLocators.textarea_messagebox)  # Presses Enter in the message box

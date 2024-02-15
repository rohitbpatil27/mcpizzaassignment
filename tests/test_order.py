import time  # Import the time module for time-related operations
import logging  # Import the logger module for logging

from conftest import *  # Import common fixtures from conftest.py
from pages import order_page  # Import order_page module
from pages.order_page import OrderPage  # Import OrderPage class from order_page module
from pages.login_page import LoginPage, baseURL  # Import LoginPage class and baseURL from login_page module
from utils.locators import CommonLocators  # Import CommonLocators from utils/locators module
from logger import setup_logging  # Import the setup_logging function from logger module

# Initialize the logger
logger = setup_logging()


@pytest.mark.usefixtures("browser_setup")
class Test_Login:
    """Test cases related to user login."""

    def setup_class(self):
        """Setup method to initialize the driver and page objects."""
        self.driver.get(baseURL)
        self.login_page = LoginPage(self.driver)
        self.order_page = OrderPage(self.driver)

    def test_launch_chatBot(self):
        """Test case to launch the chat bot."""
        logger.info("Launching chatBot...")
        self.login_page.launchChatBot()
        # Wait for the welcome message to appear
        welcome_message = self.login_page.wait_for_element(CommonLocators.welcome_msg)
        # Assert whether the welcome message is displayed
        assert welcome_message.is_displayed(), "Welcome message is not displayed"
        logger.info("Welcome message displayed successfully.")

    def test_reset_context(self):
        """Test case to reset the chat context."""
        logger.info("Resetting context...")
        self.login_page.resetMessageBox()
        # Wait for the welcome message to appear
        welcome_message = self.login_page.wait_for_element(CommonLocators.welcome_msg)
        # Assert whether the welcome message is displayed
        assert welcome_message.is_displayed(), "Welcome message is not displayed"
        logger.info("Context reset successfully.")

    def test_place_order(self):
        """Test case to place an order."""
        logger.info("Placing order...")
        self.order_page.placeOrder("I want to order pizza")

    def test_selectPizzaType(self):
        """Test case to select the pizza type."""
        logger.info("Selecting pizza type...")
        self.order_page.select_pizza_type("veg")

    def test_selectTopping(self):
        """Test case to select the pizza topping."""
        logger.info("Selecting topping...")
        self.order_page.select_topping("cheese")
        # wait for submitted successfully button
        selected_cheese = self.order_page.wait_for_element(OrderPage.button_submitted)
        # Assert whether its Submitted Successfully
        assert selected_cheese.is_displayed(), "Submit Successfully Button is not displayed"
        logger.info("Topping selected successfully.")

    def test_selectbaseSize(self):
        """Test case to select the pizza base size."""
        logger.info("Selecting base size...")
        self.order_page.select_baseSize("thick crust", "small")

    def test_validate_pizza_details(self):
        """Test case to validate pizza details."""
        logger.info("Validating pizza details...")
        expected_details = {
            "Pizza Type :": "veg",
            "Toppings :": "cheese",
            "Crust :": "thick crust",
            "Size :": "small"
        }
        assert self.order_page.validate_pizza_details(expected_details), "Pizza details do not match"
        self.order_page.wait_for_element(OrderPage.link_Confirm)
        self.login_page.webelement_click(OrderPage.link_Confirm)
        # wait for submitted successfully button
        order_placed = self.order_page.wait_for_element(OrderPage.order_placed)
        # Assert whether its Submitted Successfully
        assert order_placed.is_displayed(), "CONGRATS ! ORDER PLACED. is not displayed"
        logger.info("Pizza details validated successfully.")

    def test_provideFeedback(self):
        """Test case to provide feedback."""
        logger.info("Providing feedback...")
        self.order_page.provide_feedback("average")
        # wait for submitted successfully button
        feedback_accepted = self.order_page.wait_for_element(OrderPage.feedback_completed)
        # Assert whether its Submitted Successfully
        assert feedback_accepted.is_displayed(), "Thank You for Your Support not displayed"
        logger.info("Feedback provided successfully.")

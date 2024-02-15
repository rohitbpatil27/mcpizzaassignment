from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from utils.helper import Selenium_Helper
from utils.locators import CommonLocators

class OrderPage(Selenium_Helper):
    # Locators for elements on the order page
    link_veg = (By.XPATH, "//a[@title='veg']")
    link_nonveg = (By.XPATH, "//a[@title='non-veg']")
    checkbox_topping_cheese = (By.XPATH, "//span[normalize-space()='Cheese']")
    checkbox_topping_tomato = (By.XPATH, "//span[normalize-space()='tomato']")
    button_submit = (By.XPATH, "//button[@aria-label='Submit']")
    button_submitted = (By.XPATH, "//button[@aria-label='Submitted successfully']")
    link_Thinbase = (By.XPATH, "//a[@data-href='avaamo:#messages/new/Thin%20Crust']")
    link_Thickbase = (By.XPATH, "//a[@data-href='avaamo:#messages/new/Thick%20Crust']")
    link_sizeSmall = (By.XPATH, "//a[@title='Small']")
    link_sizeMedium = (By.XPATH, "//a[@title='Medium']")
    link_sizLarge = (By.XPATH, "//a[@title='Large']")
    message_wrap = (By.XPATH, "//div[@class='conversation-item clearfix not-mine' and contains(@aria-label, "
                              "'Your Pizza Will Look like this')]/div[@class='media']/div[@class='media-body']/div["
                              "@class='message-wrap']/p[@class='desc text-content ']")
    link_Confirm = (By.XPATH, "//a[@title='Yes']")
    order_placed = (By.XPATH, "//p[@class='desc text-content ' and contains(text(), 'CONGRATS ! ORDER PLACED .')]")
    button_thumbs_up = (By.XPATH, "//button[@class='thumbs-up locale-trans']")
    select_feedback = (By.XPATH, "//input[@role='combobox' and @class='textbox picklist-textbox avm_pick_list_input']")
    button_feedback_submit = (By.XPATH, "//button[@class='btn default_card_submit']")
    feedback_completed = (By.XPATH,"//div[@class='thankyou locale-trans' and @data-ele-name='feedback_sent' and @role='status']")

    def __init__(self, driver):
        super().__init__(driver)
        self.action_chains = ActionChains(driver)

    def placeOrder(self, orderDetails):
        """Places an order by entering order details in the message box and pressing Enter."""
        self.webelement_enter(CommonLocators.textarea_messagebox, orderDetails)
        self.webelement_enterKey(CommonLocators.textarea_messagebox)

    def select_pizza_type(self, pizza_type):
        """Selects the pizza type."""
        if pizza_type.lower() == "veg":
            self.wait_for_element(self.link_veg)
            pizza_locator = self.link_veg
        elif pizza_type.lower() == "non-veg":
            self.wait_for_element(self.link_nonveg)
            pizza_locator = self.link_nonveg
        else:
            raise ValueError("Invalid pizza type. Please specify 'veg' or 'non-veg'.")
        self.webelement_click(pizza_locator)

    def select_topping(self, topping):
        """Selects the pizza topping."""
        if topping.lower() == "cheese":
            self.wait_for_element(self.checkbox_topping_cheese)
            topping_locator = self.checkbox_topping_cheese
        elif topping.lower() == "tomato":
            self.wait_for_element(self.checkbox_topping_tomato)
            topping_locator = self.checkbox_topping_tomato
        else:
            raise ValueError("Invalid pizza topping. Please specify 'cheese' or 'tomato'.")
        self.webelement_click(topping_locator)
        self.webelement_click(self.button_submit)

    def select_baseSize(self, base, size):
        """Selects the pizza base and size."""
        if base.lower() == "thick crust":
            self.wait_for_element(self.link_Thickbase)
            base_locator = self.link_Thickbase
        elif base.lower() == "thin crust":
            self.wait_for_element(self.link_Thinbase)
            base_locator = self.link_Thinbase
        else:
            raise ValueError("Invalid pizza base. Please specify 'Thick Crust' or 'Thin Crust'.")
        self.webelement_click(base_locator)
        if size.lower() == "small":
            self.wait_for_element(self.link_sizeSmall)
            size_locator = self.link_sizeSmall
        elif size.lower() == "medium":
            self.wait_for_element(self.link_sizeMedium)
            size_locator = self.link_sizeMedium
        elif size.lower() == "large":
            self.wait_for_element(self.link_sizLarge)
            size_locator = self.link_sizLarge
        else:
            raise ValueError("Invalid pizza size. Please specify 'Small', 'Medium' or 'Large'.")
        self.webelement_click(size_locator)

    def validate_pizza_details(self, expected_details):
        """Validates the pizza details."""
        message_element = self.wait_for_element(self.message_wrap)
        message_text = message_element.text
        for key, value in expected_details.items():
            if value not in message_text:
                return False
        return True

    def provide_feedback(self, rating):
        """Provides feedback on the pizza."""
        self.wait_for_element(self.button_thumbs_up)
        self.webelement_click(self.button_thumbs_up)
        self.wait_for_element(self.select_feedback)
        self.webelement_click(self.select_feedback)
        if rating.lower() not in ["average", "good", "excellent"]:
            raise ValueError("Invalid rating. Please specify 'Average', 'Good' or 'Excellent'.")
        self.webelement_enter(self.select_feedback, rating.capitalize())
        self.action_chains.send_keys(Keys.ENTER).perform()
        self.webelement_click(self.button_feedback_submit)

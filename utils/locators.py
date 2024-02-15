from selenium.webdriver.common.by import By


class CommonLocators:
    iframe_chatbot = (By.XPATH, "//iframe[@name='avaamoIframe']")
    textarea_messagebox = (By.XPATH, "//textarea[@placeholder='Type a message...']")
    welcome_msg = (
        By.XPATH, "//p[contains(@class,'desc text-content') and contains(text(),'Welcome to McPizza Booking Journey')]")

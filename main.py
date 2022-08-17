from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class WhatsappBot:
    def __init__(self):
        self.message = "Olá sou Rocardio, é um prazer me conhecer!"

        # Name of group
        self.groups = ["Rocardio"]
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=chrome_options)
        self.driver.get("https://web.whatsapp.com/")

    def SendMessages(self):
        self.driver.get('https://web.whatsapp.com')
        time.sleep(30)
        for group in self.groups:
            input_group = self.driver.find_element("xpath", f"//span[@title='{group}']")
            time.sleep(3)
            input_group.click()

            chat_box = self.driver.find_element("xpath", f"//div[@title='Mensagem']")
            print(f'chat_box: {chat_box}')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.message)

            button_send = self.driver.find_element("xpath", "//span[@data-icon='send']")
            print(button_send)
            time.sleep(3)
            button_send.click()
            time.sleep(3)

bot = WhatsappBot()
bot.SendMessages()
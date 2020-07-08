from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class WhatsappBot:
    def __init__(self):
        self.message = "Hello World"
        self.groups = ["GRUPO TEST"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver', chrome_options=options)

    def SendMessages(self):
        # <span dir="auto" title="GRUPO TEST" class="_3ko75 _5h6Y_ _3Whw5">GRUPO TEST</span>
        # <footer tabindex="-1" class="_2vJ01"></footer>
        # <span data-testid="send" data-icon="send" class=""></span>
        # <div tabindex="-1" class="_3uMse">
        self.driver.get('https://web.whatsapp.com')
        time.sleep(30)
        for group in self.groups:
            input_group = self.driver.find_element_by_xpath(f"//span[@title='{group}']")
            time.sleep(3)
            input_group.click()

            chat_box = self.driver.find_element_by_class_name('_3uMse')
            print(f'chat_box: {chat_box}')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.message)

            button_send = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            print(button_send)
            time.sleep(3)
            button_send.click()
            time.sleep(3)
bot = WhatsappBot()
bot.SendMessages()
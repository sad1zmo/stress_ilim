from random import randrange
from selenium import webdriver


class SelDrv:

    def __init__(self):
        self.capabilities = {
            "browserName": "chrome",
            "browserVersion": "87.0",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": False,
                "enableLog": False
            }
        }
        self.driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            desired_capabilities=self.capabilities)
        self.wait = 20
        self.big_wait = 120
        self.driver.maximize_window()
        self.driver.implicitly_wait(self.wait)
        self.driver.get("http://portal-5.indusoft.ru:8093/")

    def random(self):
        return randrange(5, 15)

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from driver.css_selectors import *
import logging
import inspect


class MnemoschemeApplication:
    def __init__(self, driver):
        self.sel = driver

    def setup_factory(self):
        try:
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{button_factory}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{button_factory_sch}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{factory_table}")
        except:
            logging.warning(
                f'{self.__class__.__name__};{inspect.stack()[1].function};{inspect.stack()[0].function};Элемент не загрузился за {self.sel.wait} сек')
        finally:
            return

    def setup_phc(self):
        try:
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{button_factory}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{button_phc}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{button_phc_sch}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{phc_table}")
        except:
            logging.warning(
                f'{self.__class__.__name__};{inspect.stack()[1].function};{inspect.stack()[0].function};Элемент не загрузился за {self.sel.wait} сек')
        finally:
            return

    def setup_plc(self):
        try:
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{button_factory}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{button_plc}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{button_plc_sch}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{plc_table}")
        except:
            logging.warning(
                f'{self.__class__.__name__};{inspect.stack()[1].function};{inspect.stack()[0].function};Элемент не загрузился за {self.sel.wait} сек')
        finally:
            return

    def setup_okri(self):
        try:
            # Переходим по уровням и нажимаем AF150
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{button_factory}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{button_okri}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{button_okri_sch}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{okri_table}")
        except:
            logging.warning(
                f'{self.__class__.__name__};{inspect.stack()[1].function};{inspect.stack()[0].function};Элемент не загрузился за {self.sel.wait} сек')
        finally:
            return

    def setup_trends(self):
        try:
            # Переходим по уровням и нажимаем AF150
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{button_factory}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{button_okri}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{button_trends}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{button_trends_sch}").click()
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{trends_table}")
        except:
            logging.warning(
                f'{self.__class__.__name__};{inspect.stack()[1].function};{inspect.stack()[0].function};Элемент не загрузился за {self.sel.wait} сек')
        finally:
            return

    def setup_login(self, log, passwd):
        try:
            # Проверяем находимся ли мы на странице логина
            if self.sel.driver.find_elements(By.CSS_SELECTOR, f"{login_block}"):
                sleep(self.sel.random())
                # Вводим логин
                self.sel.driver.find_element(By.CSS_SELECTOR, f"{user_name}").send_keys(log)
                sleep(self.sel.random())
                # Вводим пароль
                self.sel.driver.find_element(By.CSS_SELECTOR, f"{user_password}").send_keys(passwd)
                sleep(self.sel.random())
                # Жмем на кнопку войти
                self.sel.driver.find_element(By.CSS_SELECTOR, f"{button_login}").click()
            else:
                return
        except:
            logging.warning(
                f'{self.__class__.__name__};{inspect.stack()[1].function};{inspect.stack()[0].function};Элемент не загрузился за {self.sel.wait} сек')
        finally:
            return

    def setup_home_button(self):
        try:
            sleep(self.sel.random())
            self.sel.driver.find_element(By.CSS_SELECTOR, f"{button_home}").click()
        except:
            logging.warning(
                f'{self.__class__.__name__};{inspect.stack()[1].function};{inspect.stack()[0].function};Элемент не загрузился за {self.sel.wait + self.sel.big_wait} сек')
        finally:
            return


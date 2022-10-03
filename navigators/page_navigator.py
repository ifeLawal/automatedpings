import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from msedge.selenium_tools import EdgeOptions
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from lxml import etree


class PageNavigator:
    def __init__(self, url: str, inputs: object, private=False) -> None:
        self.url = url
        self.inputs = inputs

        try:
            options = EdgeOptions()
            if private:
                options.set_capability(
                    name="InPrivate", value=True
                )  # options.to_capabilities()
            options.use_chromium = True
            # print(options.to_capabilities())
            self.driver = webdriver.Edge(
                "/Users/ifeoluwalawal/.wdm/drivers/edgedriver/mac64/101.0.1210.32/msedgedriver",
                capabilities={},
            )
        except Exception as ex:
            print(ex)
            firefox_profile = webdriver.FirefoxProfile()
            if private:
                firefox_profile.set_preference(
                    "browser.privatebrowsing.autostart", True
                )
            self.driver = webdriver.Firefox()

    def setup_method(self):
        self.driver.get(self.url)

    def login(
        self, url, userInputXPath="", passInputXPath="", loginButtonXPath=""
    ) -> None:
        """
        this function logs you in using the username and password fields
        """
        self.driver.get(url)
        self.fill_input(
            xPath=userInputXPath, keys=self.username, buttonXPath=userButtonXPath
        )
        self.fill_input(
            xPath=passInputXPath, keys=self.password, buttonXPath=passButtonXPath
        )
        self.click(xPath=loginButtonXPath)

    def go_to_page(self, url="") -> None:
        """
        go to page
        """
        if url == "":
            self.driver.get(self.url)
        else:
            self.url = url
            self.driver.get(url)

    def fill_input(self, xPath, keys) -> None:
        """
        input values
        """
        element = self.driver.find_element_by_xpath(xPath)
        element.send_keys(keys)

    def click(self, xPath) -> None:
        button = self.driver.find_element_by_xpath(xPath)
        button.click()

    def check_on_page(self, func, xPath) -> str:
        element = self.driver.find_element_by_xpath(xPath)
        func(element)

    def check_if_element_is_on_page(self, xPath) -> etree:
        try:
            return self.driver.find_element_by_xpath(xPath)
        except:
            return None

    def get_element_list(self, xPath) -> list:
        return self.driver.find_elements_by_xpath(xPath)

    def wait_to_load(self, waitTime=1) -> None:
        # WebDriverWait(self.driver, time)
        WebDriverWait(self.driver, waitTime)
        time.sleep(waitTime)

    def scroll_to_bottom_of_page(self) -> None:
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        
    def scroll_to_element(self, xPath) -> None:
        element = self.driver.find_element_by_xpath(xpath=xPath)
        if "firefox" in self.driver.capabilities["browserName"]:
            self.scroll_shim(element=element)

        # buffer = 40
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element).perform()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        # self.driver.execute_script("window.scrollBy(0,"+buffer+");")

    def scroll_shim(self, element) -> None:
        x = element.location["x"]
        y = element.location["y"]
        scroll_by_coord = "window.scrollTo(%s,%s);" % (x, y)
        scroll_nav_out_of_way = "window.scrollBy(0, -120);"
        self.driver.execute_script(scroll_by_coord)
        self.driver.execute_script(scroll_nav_out_of_way)

    def select_option(self, buttonXPath, optionXPath) -> None:
        self.click(buttonXPath=buttonXPath)
        element = self.driver.find_element_by_xpath(optionXPath)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element.click()

    def switch_to_iframe(self, number) -> None:
        self.driver.switch_to.frame(number)
        
    def get_element_innerhtml(self, element) -> str:
        return self.driver.execute_script("return arguments[0].innerHTML;", element)

    def get_driver(self) -> RemoteWebDriver:
        return self.driver

    def teardown_method(self) -> None:
        time.sleep(5)
        self.driver.quit()

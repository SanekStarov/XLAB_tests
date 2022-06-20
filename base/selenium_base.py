import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.remote.webelement import WebElement
from typing import List

class SeleniumBaseClass:

    def __init__(self, driver):
        # Время задержки
        delay = 10
        # Игнорирование исключений
        ignored_exception = (NoSuchElementException, StaleElementReferenceException)

        self.driver = driver
        self.__wait = WebDriverWait(driver, delay, ignored_exceptions=ignored_exception)


    def __get_locator_by(self, find_by: str) -> dict:
        find_by = find_by.lower()
        locating = {
            'xpath':By.XPATH,
            'id':By.ID,
            'name':By.NAME,
            'class_name':By.CLASS_NAME,
            'css':By.CSS_SELECTOR,
            'link_text':By.LINK_TEXT,
            'partial_link_text':By.PARTIAL_LINK_TEXT,
            'tag':By.TAG_NAME
        }
        return locating[find_by]

    def is_clickable(self, find_by, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(ec.visibility_of_element_located((self.__get_locator_by(find_by), locator)),
                                 locator_name)


    def is_present(self, find_by, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(ec.presence_of_element_located((self.__get_locator_by(find_by), locator)),
                                 locator_name)

    def is_not_present(self, find_by, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(ec.invisibility_of_element_located((self.__get_locator_by(find_by), locator)),
                                 locator_name)

    def are_visible(self, find_by, locator: str, locator_name: str = None) -> List[WebElement]:
        return self.__wait.until(ec.visibility_of_all_elements_located((self.__get_locator_by(find_by), locator)),
                                 locator_name)

    def are_present(self, find_by, locator: str, locator_name: str = None) -> List[WebElement]:
        return self.__wait.until(ec.presence_of_all_elements_located((self.__get_locator_by(find_by), locator)),
                                 locator_name).get_attribute("innerHTML")

    def get_text_from_webelements(self, elements: List[WebElement]) -> List[str]:
        return [element.text for element in elements]

    def get_element_by_text(self, elements: List[WebElement], name) -> WebElement:
        name = name.lower()
        return [element for element in elements if element.text.lower() == name][0]

    def get_current_URL(self):
        driver = self.driver
        current_URL = driver.current_url
        return current_URL

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

#Время задержки
delay = 10
#Игнорирование исключений, в будующем нужно написать обработчик с опросом каждые 0.5 сек с повторным опросом по поиску элемента на странице
ignored_exception= (NoSuchElementException, StaleElementReferenceException,)

def clickable(xpath, driver):
    element = WebDriverWait(driver,delay, ignored_exceptions=ignored_exception).until(
        ec.element_to_be_clickable((
            By.XPATH, xpath)
        )
    )
    return element
# Функция ожидания элементов
def wait_of_element(xpath, driver):
    element = WebDriverWait(driver, delay, ignored_exceptions=ignored_exception).until(
        ec.presence_of_element_located((
            By.XPATH, xpath)
        )
    )
    return element
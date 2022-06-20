from base.selenium_base import SeleniumBaseClass
from selenium.webdriver.remote.webelement import WebElement
from typing import List

from base.utils import Utils


class HomepageNav(SeleniumBaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__nav_links_header: str = 'ul.Header_header__nav_container__cClyJ>li'
        self.__nav_links_footer: str = 'div.footer__container-links-item'
        #'div.footer__container-links>div.footer__container-links-item>a.footer_description-text-link'#'p.footer_description-text.description-text'
        self.NAV_HEADER_LINKS_TEXT = 'Кредит наличными,Кредитные карты,Карты рассрочки,Займ под 0%'
        self.NAV_FOOTER_LINKS_TEXT = ''


    def get_nav_header_links(self) -> List[WebElement]:
        return self.are_visible('css', self.__nav_links_header, 'Header Navigation')

    def get_nav_footer_links(self) -> List[WebElement]:
        return self.are_present('css', self.__nav_links_footer, 'Footer Navigation')

    def get_nav_header_links_text(self) -> str:
        nav_links = self.get_nav_header_links()
        nav_links_text = self.get_text_from_webelements(nav_links)
        return Utils.join_strings(nav_links_text)

    def get_nav_footer_description(self) -> str:
        nav_links = self.get_nav_footer_links()
        footer_description = [link.text for link in nav_links]
        return Utils.join_strings(footer_description)

    def get_nav_link_by_name(self, name) -> WebElement:
        elements = self.get_nav_header_links()
        return self.get_element_by_text(elements, name)

    def get_current_window(self):
        driver = self.driver
        current_window = driver.current_window_handle
        return current_window
    #
    # def get_window_before(self, start_page):
    #     driver = self.driver
    #     window_before = driver.window_handles[-1]
    #     return window_before
    #
    # def get_window_after(self):
    #     driver = self.driver
    #     window_after = driver.window_handles[1]
    #     return window_after

    # def switch_to_window(self, start_window):
    #     driver = self.driver
    #     switch_to_window = driver.switch_to(self, start_window)
    #     return switch_to_window(start_window)


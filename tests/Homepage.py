import time
import pytest
from base.selenium_base import SeleniumBaseClass
from pom.homepage_navigation import HomepageNav


#Основные тесты тут

@pytest.mark.usefixtures('setup_with_close')
class TestLinks:
    def test_nav_links(self):
        homepage_nav = HomepageNav(self.driver)
        base_class = SeleniumBaseClass(self.driver)

        actual_links = homepage_nav.get_nav_header_links_text()
        expected_links = homepage_nav.NAV_HEADER_LINKS_TEXT
        assert expected_links == actual_links, ' Проверяем хэдэры'
        # print(homepage_nav.get_nav_footer_description())
        homepage_nav.get_nav_link_by_name('Кредитные карты').click()

        #Эксперименты
        actual_url = base_class.get_current_URL()
        expected_url = "https://test-front.onbank.online/credit_card/info"
        assert actual_url == expected_url
        time.sleep(3)
        elements = homepage_nav.get_nav_header_links()
        for element in elements:
            element.click()
            time.sleep(1)

    # def test_nav_footer_links(self):
    #     homepage_nav = HomepageNav(self.driver)
    #     base_class = SeleniumBaseClass(self.driver)
    #     print(homepage_nav.get_nav_footer_links())



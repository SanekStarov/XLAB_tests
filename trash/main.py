from selenium import webdriver
from send_telegram import send_photo_Waiting, send_photo_Acceptance
from delete_png import remove_png
from wait_functions import wait_of_element, clickable
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import autologin
import time
import pytest
import params
import web_elements
import bot_config


#Время задержки
delay = 10

#-----------------------------------------------------------------------------------------------------
# Вынесем инициализцию драйвера в отдельную фикстуру pytest
@pytest.fixture
def driver_init():
    options = webdriver.ChromeOptions()
    # options.add_argument('user-data-dir=/home/sanek02/.config/')
    options.add_argument("--auto-open-devtools-for-tabs")
    # options.headless = True
    # d = DesiredCapabilities.CHROME
    # d['loggingPrefs'] = {'browser': 'ALL'}
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options, executable_path='/usr/local/bin/chromedriver') #, desired_capabilities=d)
    driver.maximize_window()
    driver.get("https://test-front.onbank.online/?utm_source=mytarget&campaign_id=test&campaignid=test1&utm_campaign=test2&utm_term=hello&utm_content=urlss&yclid=testYCLID_1&rb_clickid=testRBCLICKID_1")
    driver.get_screenshot_as_png()
    yield driver
    driver.close()



def test_anketa_credit_card(driver_init):
    try:
        phone_number=autologin.random_phone_num_generator()
        #---------------------------------------------
        wait_of_element(xpath=web_elements.login_button_xpath,
                                       driver=driver_init).click()
        input_username = wait_of_element(xpath=web_elements.phone_xpath, driver=driver_init)
        input_username.clear()
        input_username.send_keys(phone_number)
        time.sleep(2) # чтобы записался номер в редис
        sms_code=autologin.get_code('7'+phone_number)
        input_code = wait_of_element(xpath=web_elements.sms_code_xpath, driver=driver_init)
        input_code.clear()
        input_code.send_keys(sms_code)
        time.sleep(1)
        # ---------------------------------------------
        # --------------Первый этап анкеты-------------
        # ---------------------------------------------
        clickable(xpath=web_elements.header_xpath,
                        driver=driver_init).click()
        amount_input=wait_of_element(xpath=web_elements.amount_xpath, driver=driver_init)
        amount_input.clear()
        amount_input.send_keys(params.amount_sum)
        name_input=wait_of_element(xpath=web_elements.name_xpath,
                        driver=driver_init)
        name_input.clear()
        name_input.send_keys(params.name)
        surname_input=wait_of_element(xpath=web_elements.surname_xpath,
                        driver=driver_init)
        surname_input.clear()
        surname_input.send_keys(params.surname)
        patronymic_input = wait_of_element(xpath=web_elements.patronymic_xpath,
                                        driver=driver_init)
        patronymic_input.clear()
        patronymic_input.send_keys(params.patronymic)
        #Выбор пола (гендера)
        clickable(xpath=web_elements.find_male_xpath,
                        driver=driver_init).click()
        clickable(xpath=web_elements.choose_male_xpath,
                  driver=driver_init).click()
        #Нажимаем продолжить
        wait_of_element(xpath=web_elements.continue_button_one_xpath,
                        driver=driver_init).click()
        #Закоменчено, потому что при входе с повторным номером телефона эти поля не отображаются

        # # ---------------Работаете ли вы---------------
        clickable(xpath=web_elements.work_or_not, driver=driver_init).click()
        # # ---------------------------------------------
        #
        # # ------------Работаете ли официально----------
        clickable(xpath=web_elements.official_or_not, driver=driver_init).click()
        # # ---------------------------------------------

        # ---------------------------------------------
        # --------------Второй этап анкеты-------------
        # ---------------------------------------------

        wait_of_element(xpath=web_elements.work_city_xpath,
                        driver=driver_init).clear()
        work_city= wait_of_element(xpath=web_elements.work_city_xpath,
                        driver=driver_init)
        work_city.send_keys(params.work_city)
        wait_of_element(xpath=web_elements.choose_work_city_xpath,
                        driver=driver_init).click()
        #
        wait_of_element(xpath=web_elements.work_street_xpath,
                        driver=driver_init).clear()
        work_street= wait_of_element(xpath=web_elements.work_street_xpath,
                        driver=driver_init)
        work_street.send_keys(params.work_street)
        wait_of_element(xpath=web_elements.choose_work_street_xpath,
                        driver=driver_init).click()
        #
        wait_of_element(xpath=web_elements.work_house_xpath,
                        driver=driver_init).clear()
        work_street = wait_of_element(xpath=web_elements.work_house_xpath,
                                      driver=driver_init)
        work_street.send_keys(params.work_house_number)
        wait_of_element(xpath=web_elements.choose_work_house_xpath,
                        driver=driver_init).click()
        #
        wait_of_element(xpath=web_elements.work_organization_xpath,
                        driver=driver_init).clear()
        work_organization = wait_of_element(xpath=web_elements.work_organization_xpath,
                                      driver=driver_init)
        work_organization.send_keys(params.organization_name)
        wait_of_element(xpath=web_elements.choose_work_organization_xpath,
                        driver=driver_init).click()
        # Начало работы на последнем рабочем месте (февраль, 2018)
        wait_of_element(xpath=web_elements.start_work_mounth_xpath,
                        driver=driver_init).click()
        wait_of_element(xpath=web_elements.choose_start_work_mounth_xpath,
                        driver=driver_init).click()
        wait_of_element(xpath=web_elements.start_work_year_xpath,
                        driver=driver_init).click()
        wait_of_element(xpath=web_elements.choose_start_work_year_xpath,
                        driver=driver_init).click()
        wait_of_element(xpath=web_elements.job_post_name_xpath,
                        driver=driver_init).clear()
        job_post= wait_of_element(xpath=web_elements.job_post_name_xpath,
                        driver=driver_init)
        job_post.send_keys(params.job_post_name)
        wait_of_element(xpath=web_elements.summary_income_xpath,
                        driver=driver_init).clear()
        summary_income= wait_of_element(xpath=web_elements.summary_income_xpath,
                        driver=driver_init)
        summary_income.send_keys(params.summary_income)
        wait_of_element(xpath=web_elements.continue_button_two_xpath,
                        driver=driver_init).click()
        # ---------------------------------------------
        # --------------Третий этап анкеты-------------
        # ---------------------------------------------

        #Ваше образование (Высшее)
        wait_of_element(xpath=web_elements.education_xpath,
                        driver=driver_init).click()
        wait_of_element(xpath=web_elements.choose_education_xpath,
                        driver=driver_init).click()
        #Семейное положение (Замужем/женат)
        wait_of_element(xpath=web_elements.family_status_xpath,
                        driver=driver_init).click()
        wait_of_element(xpath=web_elements.choose_family_status_xpath,
                        driver=driver_init).click()
        # Дети до 18 лет (1)
        wait_of_element(xpath=web_elements.children_xpath,
                        driver=driver_init).click()
        wait_of_element(xpath=web_elements.choose_children_xpath,
                        driver=driver_init).click()
        # Наличие автомобиля (иномарка)
        wait_of_element(xpath=web_elements.car_xpath,
                        driver=driver_init).click()
        wait_of_element(xpath=web_elements.choose_car_xpath,
                        driver=driver_init).click()
        # Наличие недвижимости (квартира)
        wait_of_element(xpath=web_elements.flat_xpath,
                        driver=driver_init).click()
        wait_of_element(xpath=web_elements.choose_flat_xpath,
                        driver=driver_init).click()

        # Нажимаем "Продолжить"
        wait_of_element(xpath=web_elements.continue_button_three_xpath,
                        driver=driver_init).click()
        # ---------------------------------------------
        # --------------Четвёртый этап анкеты----------
        # ---------------------------------------------

        #Дата рождения
        clickable(xpath=web_elements.birthdate_xpath,
                        driver=driver_init).clear()
        birthdate = wait_of_element(xpath=web_elements.birthdate_xpath,
                                   driver=driver_init)
        birthdate.send_keys('\b\b\b\b\b\b\b\b\b\b\b\b\b\b')
        birthdate.send_keys(params.birthdate)
        #Место рождения
        wait_of_element(xpath=web_elements.birthplace_xpath,
                        driver=driver_init).clear()
        birthplace = wait_of_element(xpath=web_elements.birthplace_xpath,
                                   driver=driver_init)
        birthplace.send_keys(params.birthplace)
        # Серия и номер паспорта
        wait_of_element(xpath=web_elements.passport_number_xpath,
                        driver=driver_init).clear()
        passport_number = wait_of_element(xpath=web_elements.passport_number_xpath,
                                     driver=driver_init)
        passport_number.send_keys('\b\b\b\b\b\b\b\b\b\b\b\b\b\b')
        passport_number.send_keys(params.passport_number)
        # Дата выдачи паспорта
        wait_of_element(xpath=web_elements.passport_date_xpath,
                        driver=driver_init).clear()
        passport_date = wait_of_element(xpath=web_elements.passport_date_xpath,
                                    driver=driver_init)
        passport_date.send_keys('\b\b\b\b\b\b\b\b\b\b\b\b\b\b')
        passport_date.send_keys(params.passport_date)
        # Код подразделения
        wait_of_element(xpath=web_elements.passport_code_xpath,
                        driver=driver_init).clear()
        passport_code = wait_of_element(xpath=web_elements.passport_code_xpath,
                                    driver=driver_init)
        passport_code.send_keys(params.passport_code)
        wait_of_element(xpath=web_elements.choose_passport_code_xpath,
                        driver=driver_init).click()
        #Адрес регистрации, город
        wait_of_element(xpath=web_elements.registration_city_xpath,
                        driver=driver_init).clear()
        reg_city = wait_of_element(xpath=web_elements.registration_city_xpath,
                                        driver=driver_init)
        reg_city.send_keys(params.registration_city)
        wait_of_element(xpath=web_elements.choose_registration_city_xpath,
                        driver=driver_init).click()
        # Адрес регистрации, улица
        wait_of_element(xpath=web_elements.registartion_street_xpath,
                        driver=driver_init).clear()
        reg_street = wait_of_element(xpath=web_elements.registartion_street_xpath,
                                   driver=driver_init)
        reg_street.send_keys(params.registration_street)
        wait_of_element(xpath=web_elements.choose_registartion_street_xpath,
                        driver=driver_init).click()
        # Адрес регистрации, дом
        wait_of_element(xpath=web_elements.registartion_house_xpath,
                        driver=driver_init).clear()
        reg_street = wait_of_element(xpath=web_elements.registartion_house_xpath,
                                     driver=driver_init)
        reg_street.send_keys(params.registration_house)
        wait_of_element(xpath=web_elements.choose_registartion_house_xpath,
                        driver=driver_init).click()
        # Адрес регистрации, квартира
        wait_of_element(xpath=web_elements.registartion_flat_xpath,
                        driver=driver_init).clear()
        reg_street = wait_of_element(xpath=web_elements.registartion_flat_xpath,
                                     driver=driver_init)
        reg_street.send_keys(params.registration_flat)
        wait_of_element(xpath=web_elements.choose_registartion_flat_xpath,
                        driver=driver_init).click()
        # Нажимаем "Продолжить"
        wait_of_element(xpath=web_elements.continue_button_four_xpath,
                        driver=driver_init).click()
        time.sleep(10)
        driver_init.get_screenshot_as_file("Waiting.png")
        send_photo_Waiting(chat_id=bot_config.chat_id)
        time.sleep(50)
        driver_init.get_screenshot_as_file("Acceptance.png")
        send_photo_Acceptance(chat_id=bot_config.chat_id)
        # for entry in driver_init.get_log('browser'):
        #     print(entry)
        print("\n Анкета заполнена и отправлена. Результаты высланы в телеграмм!")
        time.sleep(5)
        # Удаляем скриншоты с локальной машины
        remove_png()
    except Exception as e:
        print("\n Неудачная попытка ...", e)
        driver_init.quit()



if __name__ == '__main__':
    # test_redis_communication()
    test_anketa_credit_card(driver_init=driver_init)

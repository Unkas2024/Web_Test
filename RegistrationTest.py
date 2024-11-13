import allure
from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper
from pages.RegistrationPage import RegistrationPageHelper

Base_URL = 'https://ok.ru/'

def test_registration_page_random_country(browser):
    BasePage(browser).get_url(Base_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.click_registration()
    RegistrationPage = RegistrationPageHelper(browser)
    Selected_country_code = RegistrationPage.select_random_country()
    Actual_country_code = RegistrationPage.get_phone_field_value()
    assert Selected_country_code == Actual_country_code



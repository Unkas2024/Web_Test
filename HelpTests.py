import allure
from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.HelpPage import HelpPageHelper, HelpPageLocators
from pages.Cabinet import CabinetHelpHelper


Base_URL = 'https://ok.ru/help'

def test_help_test(browser):
    BasePage(browser).get_url(Base_URL)
    HelpPage = HelpPageHelper(browser)
    HelpPage.scrollToitem(HelpPageLocators.ADVERTISEMENT_CABINET)
    CabinetHelpHelper(browser)




import allure

from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper
from pages.RecoveryPage import RecoveryPageHelper

Base_URL = 'https://ok.ru/'
Login_Text = 'email'
Password_Text = '1'

@allure.suite('Проверка восстановления пользователя')
@allure.title('Проверка перехода к восстановлению')
def test_go_to_recovery(browser):
    BasePage(browser).get_url(Base_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.type_login(Login_Text)
    for i in range(3):
        LoginPage.type_password(Password_Text)
        LoginPage.click_login()

    LoginPage.click_recovery()
    RecoveryPageHelper(browser)



#    LoginPage.type_password(Password_Text)
#    LoginPage.click_login()
#    LoginPage.type_password(Password_Text)
#    LoginPage.click_login()
#    LoginPage.type_password(Password_Text)
#    LoginPage.click_login()





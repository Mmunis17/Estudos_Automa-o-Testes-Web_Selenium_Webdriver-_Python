from http import HTTPStatus
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC #as EC deixa o campo mais minimalista
from webdriver_manager.chrome import ChromeDriverManager
import conftest  # type: ignore # global
##from ..Pages.login_page import LoginPage
#from pages.login_page import LoginPage # type: ignore



@pytest.mark.usefixtures("setup_teardown") #pega a referencia da conftest
@pytest.mark.login
class TestCT02: #nome da class ser o mesmo nome do cenario de teste o id
    def test_ct02_login_valido(self):
        driver = conftest.driver # por ser uma variavel
      
        ##login_page = LoginPage()
        
        #self.fazer_login(login_page)

        ##login_page.fazer_login("standard_user", "secret_sauce")
        
        ##acessando a pagina, com usuário, senha e clique
        driver.find_element(By. ID, "user-name").send_keys("standard_user")
        driver.find_element(By. ID, "password").send_keys("secret_sauce")
        driver.find_element(By. ID, "login-button").click ()

        #mapear o campo de products verificando se caiu no campo
        assert driver.find_element(By. XPATH, "//span [@class='title']").is_displayed()

        time.sleep(5)
        #boas praticas, sempre deixar uma linha em branco

        driver.close()

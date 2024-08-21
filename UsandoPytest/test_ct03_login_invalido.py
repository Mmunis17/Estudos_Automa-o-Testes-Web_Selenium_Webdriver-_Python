import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC #as EC deixa o campo mais minimalista
import conftest #global


@pytest.mark.usefixtures("setup_teardown") #pega a referencia da conftest
@pytest.mark.login
class TestCT03: #nome da class ser o mesmo nome do cenario de teste o id
    def test_ct03_login_invalido(serf):

        driver = conftest.driver # por ser uma variavel
        #acessando a pagina, com usuário, senha e clique
        driver.find_element(By. ID, "user-name").send_keys("standard_user")
        driver.find_element(By. ID, "password").send_keys("senhaerrada")
        driver.find_element(By. ID, "login-button").click ()

        #mapear o campo de products verificando se caiu no campo, não mostra campo [0] por ser uma lista, no python ele retorna a lista ["e1", "e2", "e3"]
        assert len(driver.find_elements(By. XPATH, "//span [@class='title']"))  == 0

        time.sleep(2)
        #boas praticas, sempre deixar uma linha em branco

 
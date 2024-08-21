import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC #as EC deixa o campo mais minimalista
import conftest #global

import sys #paranaué
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.login_page import LoginPage #paranaué

@pytest.mark.usefixtures("setup_teardown") #pega a referencia da conftest
@pytest.mark.carrinho #para rodar apenas esse teste
class TestCT01: #nome da class ser o mesmo nome do cenario de teste o id
    def test_ct01_adicionar_produtos_carrinho(serf):
        
        driver = conftest.driver # por ser uma variavel
        
        login_page = LoginPage() #trazendo o arquivo pages
        
        login_page.fazer_login("standard_user", "secret_sauce") #função pages
        
        #fazendo login, acessando a pagina, com usuário, senha e clique
        #driver.find_element(By. ID, "user-name").send_keys("standard_user")
        #driver.find_element(By. ID, "password").send_keys("secret_sauce")
        #driver.find_element(By. ID, "login-button").click ()

        # Adicionando a mochila - para achar e clicar no produto - linha21
        #adicionar o produto no carrinho com mapeamento unico, ja que cada botão tem o id unico do produto - linha 22
        driver.find_element(By. XPATH, "//*[@class='inventory_item_name ' and text()='Sauce Labs Backpack']").click()
        driver.find_element(By. XPATH, "//*[text()='Add to cart']").click()

        #verificar no carrinho se foi adicionado o produto e verificar campos - mochila
        driver.find_element(By. XPATH, "//*[@class='shopping_cart_link']").click()
        assert driver.find_element(By. XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()

        #clicando para voltar e adicionar mais um produto
        driver.find_element(By. ID, "continue-shopping").click()

        #aproveita o codigo de add de mais um produto, no caso a bike
        driver.find_element(By. XPATH, "//*[@class='inventory_item_name ' and text()='Sauce Labs Bike Light']").click()
        driver.find_element(By. XPATH, "//*[text()='Add to cart']").click()

        #verificar no carrinho se os dois produtos estão no carrinho
        driver.find_element(By. XPATH, "//*[@class='shopping_cart_link']").click()
        assert driver.find_element(By. XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()
        assert driver.find_element(By. XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Bike Light']").is_displayed()

        #boas praticas, sempre deixar uma linha em branco


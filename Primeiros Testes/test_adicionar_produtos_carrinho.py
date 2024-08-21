from http import HTTPStatus
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC #as EC deixa o campo mais minimalista
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()
driver.maximize_window()
driver.get ("https://www.saucedemo.com/")

#fazendo login, acessando a pagina, com usuário, senha e clique
driver.find_element(By. ID, "user-name").send_keys("standard_user")
driver.find_element(By. ID, "password").send_keys("secret_sauce")
driver.find_element(By. ID, "login-button").click ()

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

driver.close()

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
time.sleep(5)
# Adicionando a mochila - para achar e clicar no produto - linha21
#adicionar o produto no carrinho com mapeamento unico, ja que cada botão tem o id unico do produto - linha 22
driver.find_element(By. XPATH, "//*[@class='inventory_item_name ' and text()='Sauce Labs Backpack']").click()
driver.find_element(By. XPATH, "//*[text()='Add to cart']").click()
time.sleep(5)
#verificar no carrinho se foi adicionado o produto e verificar campos - mochila
driver.find_element(By. XPATH, "//*[@class='shopping_cart_link']").click()
assert driver.find_element(By. XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()
time.sleep(5)

#clicando no botão Checkout
driver.find_element(By. ID, "checkout").click()

#preenchendo os campos
driver.find_element(By. ID, "first-name").send_keys("Munis de Oliveira")
driver.find_element(By. ID, "last-name").send_keys("MaYaRa")
driver.find_element(By. ID, "postal-code").send_keys("03977210")
time.sleep(5)
#clciando no botão continue
driver.find_element(By. ID, "continue").click()
time.sleep(5)
#clicando no botão finish
driver.find_element(By. ID, "finish").click()
time.sleep(5)
#verificando se cheguei no campo de fim do compra
assert driver.find_element(By. XPATH, "//*[text()='Thank you for your order!']").is_displayed()
time.sleep(5)
#boas praticas, sempre deixar uma linha em branco

driver.close()

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
# Adicionando produto 1 - para achar e clicar no produto - linha21
#adicionar o produto no carrinho com mapeamento unico, ja que cada botão tem o id unico do produto - linha 22
driver.find_element(By. XPATH, "//*[@class='inventory_item_name ' and text()='Sauce Labs Bolt T-Shirt']").click()
driver.find_element(By. XPATH, "//*[text()='Add to cart']").click()
time.sleep(3)
#ir para o carrinho
#verificar no carrinho se foi adicionado o produto 1 e verificar campos 
driver.find_element(By. XPATH, "//*[@class='shopping_cart_link']").click()
assert driver.find_element(By. XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Bolt T-Shirt']").is_displayed()
time.sleep(3)
#clicando para voltar e adicionar mais um produto
driver.find_element(By. ID, "continue-shopping").click()
time.sleep(3)
#aproveita o codigo de add de mais um produto 2
driver.find_element(By. XPATH, "//*[text()='Test.allTheThings() T-Shirt (Red)']").click()
driver.find_element(By. XPATH, "//*[text()='Add to cart']").click()
time.sleep(3)
#verificar no carrinho se os dois produtos estão no carrinho
driver.find_element(By. XPATH, "//*[@class='shopping_cart_link']").click()
assert driver.find_element(By. XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Bolt T-Shirt']").is_displayed()
assert driver.find_element(By. XPATH, "//*[@class='inventory_item_name' and text()='Test.allTheThings() T-Shirt (Red)']").is_displayed()
time.sleep(3)

#agora vamos para fechar o pedido clicando no checkout
driver.find_element(By. ID, "checkout").click()

#preenchendo os campos
driver.find_element(By. ID, "first-name").send_keys("Munis da Silva")
driver.find_element(By. ID, "last-name").send_keys("Arlinda")
driver.find_element(By. ID, "postal-code").send_keys("03977211")
time.sleep(3)
#clciando no botão continue
driver.find_element(By. ID, "continue").click()
time.sleep(3)
#clicando no botão finish
driver.find_element(By. ID, "finish").click()
time.sleep(3)
#verificando se cheguei no campo de fim do compra
assert driver.find_element(By. XPATH, "//*[text()='Thank you for your order!']").is_displayed()
time.sleep(3)

#time.sleep(3) não são necessario, estão para verificar se esta funcionando

#boas praticas, sempre deixar uma linha em branco

driver.close()

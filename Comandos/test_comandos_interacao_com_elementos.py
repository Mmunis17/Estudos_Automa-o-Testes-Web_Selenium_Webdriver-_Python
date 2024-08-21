from http import HTTPStatus
from lib2to3.pgen2 import driver
import time
from selenium import webdriver
from selenium.webdriver.common.by import By 
#estanciando o chrome - navegador de acesso
browser = webdriver.Chrome()

browser.maximize_window()
#acessando o site do google
browser.get ("https://www.saucedemo.com/")
#tempo para pagina ficar aberta
time.sleep(5)

#find_element()
username = browser.find_element(By.ID, "user-name")
password = browser.find_element(By.ID, "password")
btn_login = browser.find_element(By.ID, "login-button")

#acessando o site e preenchendo os campos e clicando no botão de login

# send_keys()
username.send_keys("standard_user")
password.send_keys("secret_sauce")

# click()
btn_login.click()
time.sleep(15)

# text -- buscar o texto
product_title = browser.find_element(By.XPATH, "//span[@class='title']")
print (product_title.text)
assert product_title.text == "Products" # == realiza a comparação se é verdedade e escrever exatamente do jeito que esta

# get_attribute() esta achando o atributo e funciona com qualquer atributo é só mapear
img_backpack = browser.find_element(By.XPATH, "(//img[@class='inventory_item_img'])[1]")
print (img_backpack.get_attribute("alt"))
assert img_backpack.get_attribute("alt") == "Sauce Labs Backpack"

#assert img_backpack.is_displayed()
assert not img_backpack.is_displayed() #para saber que o elemento não esta presente

#boas praticas, sempre deixar uma linha em branco

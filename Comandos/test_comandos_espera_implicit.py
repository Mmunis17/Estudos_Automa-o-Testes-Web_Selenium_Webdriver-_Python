from http import HTTPStatus
from lib2to3.pgen2 import driver
import time
from selenium import webdriver
from selenium.webdriver.common.by import By 
#estanciando o chrome - navegador de acesso
browser = webdriver.Chrome()
browser.implicitly_wait(12)

browser.maximize_window()
#acessando o site do google
browser.get ("https://chercher.tech/practice/implicit-wait-example")

checkbox = browser.find_element(By.XPATH, "//input[@type='checkbox']")
assert checkbox.is_displayed()

time.sleep (3)
print ("Checkbox está na tela!")

#boas praticas, sempre deixar uma linha em branco


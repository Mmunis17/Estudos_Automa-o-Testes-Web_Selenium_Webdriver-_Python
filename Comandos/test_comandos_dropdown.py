from http import HTTPStatus
from lib2to3.pgen2 import driver
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC #as EC deixa o campo mais minimalista
from webdriver_manager.chrome import ChromeDriverManager

#estanciando o chrome - navegador de acesso
browser = webdriver.Chrome()
browser.maximize_window()
#acessando o site do google
browser.get ("https://chercher.tech/practice/practice-dropdowns-selenium-webdriver")

#mapear o primeiro dropdown e no caso para um dropdown, precisamos usar select
dropdown_products = Select(browser.find_element(By.XPATH, "//select[@id='first']"))
#esse é o tipo de select que precisa fazer, tem varias opções e no caso de texto informar
dropdown_products.select_by_visible_text("Google")

time.sleep(5)

dropdown_animals = Select(browser.find_element(By.ID, "animals"))
dropdown_animals.select_by_visible_text("Avatar")

time.sleep(5)
#por seleção na oredem o dropdown
dropdown_animals.select_by_index(2)

time.sleep(2)

#seletor multiplo
dropdown_food = Select(browser.find_element(By.XPATH, "//select[@id='second']"))
dropdown_food.select_by_visible_text("Pizza")
time.sleep(2)
dropdown_food.select_by_visible_text("Bonda")

##pode ser usado dentro de uma função, criando um metodo

#tempo para pagina ficar aberta
time.sleep(3)
#boas praticas, sempre deixar uma linha em branco


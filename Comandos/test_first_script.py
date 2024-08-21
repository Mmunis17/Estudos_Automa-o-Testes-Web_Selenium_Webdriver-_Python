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
#acessando o site que deseja
browser.get ("https://gimbaempresas.com.br")
#tempo para pagina ficar aberta
time.sleep(5)
#boas praticas, sempre deixar uma linha em branco


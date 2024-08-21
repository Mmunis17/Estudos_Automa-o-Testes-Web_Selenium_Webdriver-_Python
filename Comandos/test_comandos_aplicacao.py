from http import HTTPStatus
from lib2to3.pgen2 import driver
import time
from selenium import webdriver
#estanciando o chrome - navegador de acesso
browser = webdriver.Chrome()
#acessando o site do google

# maximize_window() - aumenta o tamanho da pagina
browser.maximize_window()
#acessando o site
browser.get ("https://www.saucedemo.com/")

#vai da um print no titulo da pagina - #title
print("O titulo da pagina é:",browser.title)

#vai da um print na url da pagina - #current_url
print("A url da pagina é:",browser.current_url)

#vai da um print do codigo da pagina - #page_source
print("O codigo-fonte da pagina é:",browser.page_source)

#tempo aberto
time.sleep(2)
#boas praticas, sempre deixar uma linha em branco


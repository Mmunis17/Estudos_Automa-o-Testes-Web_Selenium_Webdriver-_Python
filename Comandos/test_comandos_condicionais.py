from http import HTTPStatus
from lib2to3.pgen2 import driver
import time
from selenium import webdriver
from selenium.webdriver.common.by import By 
#estanciando o chrome - navegador de acesso
browser = webdriver.Chrome()
# maximize_window() - aumenta o tamanho da pagina
browser.maximize_window()
#acessando o site do google
browser.get ("https://demo.applitools.com/")
#tempo para pagina ficar aberta
time.sleep(3)

#criando o variavel username e mapear
username = browser.find_element(By.ID, "username")

#criando o variavel, mas o que ela é checkbox e mapear // recomendação seja o nome grande para facil explicação
checkbox_remember_me = browser.find_element(By.XPATH, "//*[@type='checkbox']")

#retona se é verdadeiro o falso
# is_displayed()
print(username.is_displayed())
assert username.is_displayed() #informa se veio verdadeiro

# is_enabled()
print(username.is_enabled()) #se o campo esta habilitado
assert username.is_enabled() #informa se veio verdadeiro

# is_selected()
print(checkbox_remember_me.is_selected()) #verificação do checkbox em branco
assert not checkbox_remember_me.is_selected() #assert só traz informação verdadeira como esta em branco, por isso o not

#Clicando no checkbox
time.sleep(2) #visualizar antes do clique
checkbox_remember_me.click()
time.sleep(2) #visualizar depois do clique #não se usa muito o time... hahahah

# is_selected()
print(checkbox_remember_me.is_selected())
assert checkbox_remember_me.is_selected() #preenchendo o checkbox

#boas praticas, sempre deixar uma linha em branco


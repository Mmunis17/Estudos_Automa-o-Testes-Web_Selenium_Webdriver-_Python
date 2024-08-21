from http import HTTPStatus
from lib2to3.pgen2 import driver
import time
from selenium.webdriver.common.by import By 
#importação dos elementos

from selenium import webdriver
#estanciando o chrome - navegador de acesso
browser = webdriver.Chrome()
#acessando o site do google

# maximize_window() - aumenta o tamanho da pagina
browser.maximize_window()
#acessando o site
browser.get ("https://www.saucedemo.com/")

#find_element - localizar um elemento, ele criou uma variavel (username) e foi buscar o elemento e utiliza o Locators
#username = browser.find_element(By.ID, "user-name")

#find_element - localizar um elemento, ele criou uma variavel (password) e foi buscar o elemento e utiliza o Locators
#password = browser.find_element(By.ID, "password")

#send_keys - comando de enviar a teclas, que escreve no campo, usando a variavel, pois o elemento ja esta atribuido a variavel
#username.send_keys("standard_user") 
#password.send_keys("secret_sauce")

#find_elements - traz mais de um elemento, e quando não encotra o elemento, ele não da erro e retorna uma lista sem elemento e acha campos em comum
#auth_fields - variavel de campos de autenticação, onde traz uma nova coisa
#quando utiliza "", ao usar o xpath, precisa usar simples
auth_fields = browser.find_elements(By.XPATH, "//*[@class='input_error form_input']")

print(auth_fields)
#print mais o len ver tamanho da variavel - mostrando quantos elementos tem
print(len(auth_fields))

#assert - quero verificar se carrou dois campos de autenticação, é possivel colocar mensagem de erro forçando após a ,
assert len(auth_fields) == 2, "O número de elementos encontrados é deferente do esperados" #caso eu altere para diferente de 2

#tempo aberto
time.sleep(3)

#fecha de forma correta
browser.quit

#boas praticas, sempre deixar uma linha em branco


from http import HTTPStatus
from lib2to3.pgen2 import driver
import time
from selenium import webdriver

#estanciando o chrome - navegador de acesso
browser = webdriver.Chrome()

# maximize_window() - aumenta o tamanho da pagina
browser.maximize_window()

#acessando o site do google
browser.get ("https://gimbaempresas.com.br")

#atualiza a pagina
browser.refresh()

#teste de voltar para usar back, mais uma pagina
browser.get ("https://gimba.com.br")

#tempo para pagina ficar aberta
time.sleep(5)

#back() ele volta para primeira pagina
browser.back()
#teste
time.sleep(3)

#forward() ele volta para segunda pagina
browser.forward()
#teste
time.sleep(3)

#vai abrir uma nova aba
browser.switch_to.new_window ("tab") 
time.sleep(3)

# close() vai fechar a nova aba
browser.close()

#vai abrir uma nova aba -- teste quit
#browser.switch_to.new_window ("tab") 
#vai abrir uma nova aba -- teste quit
#browser.switch_to.new_window ("tab") 
#time.sleep(3)

# quit() fecha todas as abas e é uma boa pratica usar sempre
browser.quit()

#boas praticas, sempre deixar uma linha em branco


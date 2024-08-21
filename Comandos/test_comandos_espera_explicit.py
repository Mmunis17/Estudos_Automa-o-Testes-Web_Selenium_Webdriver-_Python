from http import HTTPStatus
from lib2to3.pgen2 import driver
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#estanciando o chrome - navegador de acesso
browser = webdriver.Chrome()
browser.maximize_window()

#acessando o site
browser.get ("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")

#uso da espera explicita, onde espera o que quiser, mas precisa ter um time out, onde você coloca um tempo maximo, tempo acima do normal
wait = WebDriverWait(browser, 30)

#Alert is present, botão 1
#uso elemento alert e não precisa jogar em uma variavel
# browser.find_element(By.ID, "alert").click()

#esperta até=until
#wait.until(EC.alert_is_present())

#-----

#Tex_to_be_present_in_element - texto esta presnte no elemento - botão 2
#browser.find_element(By.ID, "populate-text").click()
#espera o texto pelo  locator um xpath e o texto esperado
#wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*[@class='target-text']"), "Selenium Webdrive"))

#mapeando elemento
#target_text = browser.find_element(By.XPATH,  "//*[@class='target-text']").text
#assert target_text == "Selenium Webdriver"

#-----

#botão aparece depois de 10 segundos e seja cricavel - element_to_be_clickable
##browser.find_element(By.ID, "display-other-button").click()
##wait.until(EC.element_to_be_clickable((By.ID, "hidden")))

#botão aparece depois de 10 segundos e seja cricavel
#browser.find_element(By.ID, "enable-button").click()
#wait.until(EC.element_to_be_clickable((By.ID, "disable")))

#nesse precisa declarar elemento - Verifica se seleciona o elemento checkbox -
checkbox = browser.find_element(By.ID, "ch")
browser.find_element(By.ID, "checkbox").click()
wait.until(EC.element_to_be_selected(checkbox))

#Exites muito mas condições usando o EC. caso precise

time.sleep(2)

#boas praticas, sempre deixar uma linha em branco


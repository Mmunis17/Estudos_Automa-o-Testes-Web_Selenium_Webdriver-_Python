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
#acessando o site 
browser.get ("https://chercher.tech/practice/frames")

##antes de inserir o texto, achar o iframe - linha 20
iframe1 = browser.find_element(By.ID, "frame1")
## para achar o frame que foi mapeado, sempre precisa achar o frame
browser.switch_to.frame(iframe1)
browser.find_element(By.XPATH, "//*[@id='topic']/following-sibling::input").send_keys("iFrame1")

time.sleep(3)

##esse find_elemente linha 25, não poderia estar antes do switch_to.frame(iframe1) linha 19
iframe3 = browser.find_element(By.ID, "frame3")
browser.switch_to.frame(iframe3)
checkbox = browser.find_element(By.XPATH, "//*[@type='checkbox']")
checkbox.click()

time.sleep(3)

## como voltar para a raiz da pagina, como se estivesse no começo antes de ter feito qualquer frame
browser.switch_to.default_content()

iframe2 = browser.find_element(By.ID, "frame2")
browser.switch_to.frame(iframe2)
dropdown_animals = Select(browser.find_element(By.ID, "animals"))
dropdown_animals.select_by_visible_text("Avatar")

#tempo para pagina ficar aberta
time.sleep(5)
#boas praticas, sempre deixar uma linha em branco


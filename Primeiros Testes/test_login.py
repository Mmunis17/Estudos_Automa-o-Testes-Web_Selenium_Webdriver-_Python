from http import HTTPStatus
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC #as EC deixa o campo mais minimalista
from webdriver_manager.chrome import ChromeDriverManager
import conftest  # global

driver = webdriver.Chrome()
driver.maximize_window()
driver.get ("https://www.saucedemo.com/")

#acessando a pagina, com usuário, senha e clique
driver.find_element(By. ID, "user-name").send_keys("standard_user")
driver.find_element(By. ID, "password").send_keys("secret_sauce")
driver.find_element(By. ID, "login-button").click ()

#mapear o campo de products verificando se caiu no campo
assert driver.find_element(By. XPATH, "//span [@class='title']").is_displayed()

time.sleep(5)
#boas praticas, sempre deixar uma linha em branco

driver.close()

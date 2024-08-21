from http import HTTPStatus
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC #as EC deixa o campo mais minimalista
from webdriver_manager.chrome import ChromeDriverManager
import conftest

driver = webdriver.Chrome()
driver.maximize_window()
driver.get ("https://www.saucedemo.com/")

#fazendo login, acessando a pagina, com usuário, senha e clique
driver.find_element(By. ID, "user-name").send_keys("standard_user")
time.sleep(3)
driver.find_element(By. ID, "password").send_keys("rjenbjjrbjbbjvbhbvhbdljweihuhweujfb") #senha errada
time.sleep(3)
driver.find_element(By. ID, "login-button").click ()
time.sleep(2)

#verificar no login se apresentou a mensagem de erro
assert driver.find_element(By. XPATH, "//*[@class='error-message-container error']").is_displayed()
time.sleep(5)

driver.close()

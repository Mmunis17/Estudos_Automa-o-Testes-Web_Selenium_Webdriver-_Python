import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


# variavel definida de forma global, no python nem sempre precisa, mas é bom por usar esses testes em outros lugares
driver: webdriver.Remote


@pytest.fixture
# função
def setup_teardown():

    # setup
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get ("https://www.saucedemo.com/")

    # run test - vai execultar realmente o teste, dentro do arquivo ex. test.login
    yield 

    # teardown - vai encerrar o teste
    driver.quit

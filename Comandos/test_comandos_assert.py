#O Assert sempre verifica se o retorno da condição é True (Verdadeiro)
##assert True

#assert numbers
#false
##num_esperado = 1
##num_obtido = 2

#sempre depois da virgula com "" é possivel incluir uma mensagem, uso de {} deixa a string formatada, pode usar sinais (>; <; ==; !=)
##assert num_esperado == num_obtido, f"Esperado {num_esperado}. Atual {num_obtido}."   

#assert text
##text_esperado = "Selenium Webdriver"
##text_obtido = "Selenium webdriver"
#.lower - deixa tudo minusculo, assim deixando tudo igual
##assert text_esperado.lower() == text_obtido.lower(), f"Esperado {text_esperado}. Atual {text_obtido}."   

#assert text in string - procura se existe a palavra - ' aspas simples para melhorar leitura - not in ou in
from lib2to3.pgen2 import driver


text_esperado = "Seleniumzzzzz"
text_obtido = "Selenium webdriver"
assert text_esperado not in text_obtido, f"Esperado '{text_esperado}'. Atual '{text_obtido}'." 

#assert is_displayed/is_enabled/is_selected - 3 opção e sempre retona true ou false
#esta no aquivo test_comandos_interacao_com_elementos, linha 39 e 40

#boas praticas, sempre deixar uma linha em branco


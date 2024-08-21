import pytest

@pytest.mark.simulacao


#adicionar marcadores, nos testes --- linhas 1 e 4 e sempre deixar linha em branco
#um teste pode ter mais de um mark @pytest.mark.simulacao @pytest.mark.cadastro

#funções do pytest isolado, criando metodos de teste

#sempre que usar uma class (precisa começar com Test), precisa usar o self
class TestSimulacao():
#essas são duas formas iniciais
#metodo + test_
    def test_simulacao_1(self):
        assert 1 == 1

    @pytest.mark.simulacao
    @pytest.mark.skip  ##para pular teste
    def test_simulacao_2(self):
        assert 2 == 2

# ------ \\\\\\ powershell //////--------

# - pasta - cd C:\Users\89038\Desktop\AutomacaoTeste\Estudos\Comandos

# pytest test_simulacao_pytest.py - execulta

#-v  #aumenta a verbosidade do teste, então alem dos dois pontos(que deu bom), ele aumenta a quantidade de informação que é disponibilizada
##PS C:\Users\89038\Desktop\AutomacaoTeste\Estudos> pytest -v test_simulacao_pytest.py
     
#:: chama a função
##pytest test_simulacao_pytest.py::test_simulacao_1
        
## -m #lina 4 - trazendo marcação - assim executando tudo o que tem na pasta
#pytest -m simulacao ##roda tudo que estiver na pasta, sem indicar arquivo
#pytest test_simulacao_pytest.py -m simulacao ## roda o arquivo especifico
#pytest test_simulacao_pytest.py -v -m simulacao ##melhora a verbosidade do teste


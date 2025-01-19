from .calculator_4 import Calculator4
from typing import Dict, List
from src.errors.http_bad_request import HttpBadRequestError
from pytest import raises


# Mock da requisição
class MockRequest:
    def __init__(self,body: Dict) -> None:
        self.json = body

# Mock do driver handler com erro
class MockDriverHandlerError:
    def average(self, numbers: List[float]) -> float:
        return None
    

# Mock do driver handler sem erro
class MockDriverHandler:
    def average(self, numbers: List[float]) -> float:
       return 2.5
    
# Teste para erro no cálculo
def test_calculate_average_error():
    mock_request = MockRequest({"numbers": [1, 2, 3, 4]})
    calculator_4 = Calculator4(MockDriverHandlerError())  

    with raises(HttpBadRequestError) as excinfo:
        calculator_4.calculate_average(mock_request)

    assert str(excinfo.value) == "Média inválida calculada."

# Teste para o sucesso no cálculo
def test_calculate_average():
    mock_request = MockRequest({"numbers": [1, 2, 3, 4]})
    calculator_4 = Calculator4(MockDriverHandler())  

    response = calculator_4.calculate_average(mock_request)

    assert response == {'data': {'Calculator': 4, 'average': 2.5}}



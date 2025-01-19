from flask import request as FlaskRequest
from typing import Dict,List
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from src.errors.http_bad_request import HttpBadRequestError
from src.drivers.interfaces.driver_handler_interface import DriverhandlerInterface


class Calculator4:
    def __init__(self, driver_handler: DriverhandlerInterface):
        self.__driver_handler = driver_handler
    def calculate_average(self, request: FlaskRequest) -> Dict:  #type:ignore
        body = request.json
        input_data = self.__validate_body(body)

        average = self.__average(input_data)
        response = self.__format_response(average)

        return response







    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("Body mal formatado")
    
        input_data = body["numbers"]
    
    # Verifica se é uma lista e se todos os elementos são números
        if not isinstance(input_data, list) or not all(isinstance(num, (int, float)) for num in input_data):
            raise HttpUnprocessableEntityError("Lista de números não fornecida ou inválida")

        return input_data


    def __average(self, numbers: List[float]) -> float:
        media = self.__driver_handler.average(numbers)
        self.__verify_results(media)

        return media
    
    def __verify_results(self, average: float) -> None:
        if average is None or isinstance(average, str):
            raise HttpBadRequestError("Média inválida calculada.")
        

    def __format_response(self, average: float) -> Dict:
        return {
            "data": {
                "Calculator": 4,
                "average": round(average, 2)
            }
        }
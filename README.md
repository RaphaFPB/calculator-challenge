# Calculator Challenge 🚀

Este é um projeto desenvolvido como parte de um desafio para implementar uma nova funcionalidade em uma API Flask. O desafio consistia em adicionar uma rota que calcula a média entre uma lista de números enviada via requisição POST, seguindo boas práticas de programação.

## 🔧 Funcionalidades Implementadas

- **Rota `/calculator_4`**:
  - Aceita uma requisição POST com um corpo no formato JSON contendo uma lista de números.
  - Retorna a média da lista, arredondada para duas casas decimais.
  - **Exemplo de corpo da requisição**:
    ```json
    {
        "numbers": [1, 2, 3, -10]
    }
    ```
  - **Exemplo de resposta de sucesso**:
    ```json
    {
        "data": {
            "Calculator": 4,
            "average": -1.0
        }
    }
    ```
  - **Tratamento de erros**:
    - Requisições mal formatadas (ex.: ausência da chave `"numbers"`) retornam erro `422 Unprocessable Entity`.
    - Caso a lista contenha valores inválidos, como strings ou objetos, o erro `422 Unprocessable Entity` também é retornado.
    - Se ocorrer um erro no cálculo (ex.: driver retornando valores inválidos), o erro `400 Bad Request` é retornado com uma mensagem clara.

## 📂 Estrutura do Projeto

O projeto foi desenvolvido com uma arquitetura modular, dividindo responsabilidades em arquivos e pastas específicos:

```plaintext
calculator-challenge/
├── run.py                           # Arquivo principal para executar o servidor Flask
├── README.md                        # Documentação do projeto
├── src/
│   ├── calculators/
│   │   ├── __init__.py              # Inicialização do módulo calculators
│   │   ├── calculator_4.py          # Lógica da rota e do cálculo da média
│   │   └── calculator_4_test.py     # Testes unitários para a rota calculator_4
│   ├── drivers/
│   │   ├── __init__.py              # Inicialização do módulo drivers
│   │   ├── numpy_handler.py         # Implementação do driver usando numpy
│   │   └── interfaces/
│   │       ├── __init__.py          # Inicialização do módulo interfaces
│   │       └── driver_handler_interface.py # Interface para implementação de drivers
│   ├── errors/
│   │   ├── __init__.py              # Inicialização do módulo errors
│   │   ├── error_controller.py      # Controlador centralizado para gerenciamento de erros
│   │   ├── http_bad_request.py      # Classe para erro HTTP 400
│   │   └── http_unprocessable_entity.py # Classe para erro HTTP 422
│   ├── main/
│   │   ├── __init__.py              # Inicialização do módulo main
│   │   ├── factories/
│   │   │   ├── __init__.py          # Inicialização do módulo factories
│   │   │   └── calculator4_factory.py # Factory para criação de instâncias do calculator_4
│   │   ├── routes/
│   │   │   ├── __init__.py          # Inicialização do módulo routes
│   │   │   └── calculators.py       # Definição de rotas da aplicação
│   │   └── server/
│   │       ├── __init__.py          # Inicialização do módulo server
│   │       └── server.py            # Configuração do servidor Flask


## 🛠️ Tecnologias Utilizadas

- **Python 3.11**
- **Flask** para criação da API.
- **Pytest** para testes unitários.
- **Mocks** para simular o comportamento do driver no teste.

## 🧪 Testes

Os testes unitários foram desenvolvidos para garantir a confiabilidade e cobertura das funcionalidades:
1. **Teste de sucesso**: Verifica se a média é calculada corretamente, incluindo números negativos.
2. **Teste de erro**: Garante que a aplicação trata corretamente erros no cálculo ou no formato da requisição.

📋 Requisitos Atendidos
 Nova rota /calculator_4 com cálculo da média.
 Tratamento de erros para entradas mal formatadas.
 Testes unitários para cenários de sucesso e falha.
 Arquitetura modular com separação de responsabilidades.
✍️ Autor
RaphaFPB
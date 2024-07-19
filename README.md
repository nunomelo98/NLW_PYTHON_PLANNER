# Planner App API
Backend do Planner, uma aplicação de gerenciamento de viagens.

## Ferramentas
- Python
- Flask
- pytest
- virtualvenv
- Pylint
- requests
- Swagger

## Aprendizados importantes
- Criação de uma REST API utilizando python e Flask
- Criação de testes unitários utilizando Pytest
- Criação de um ambiente virtual utilizando virtualvenv
- Conexão com envio de emails utilizando o nodemailer
- Criação de emails utilizando o nodemailer
- Criação de um código com padrões de qualidade utilizando Pylint
- Aplicações de princípios SOLID
- Criação de documentação com Swagger


## Como usar

### Pré-requisitos
- python
- pip

### Instalação

1. Clone o repositório:
```sh
git clone https://github.com/nunomelo98/NLW_PYTHON_PLANNER.git
cd NLW_PYTHON_PLANNER
```

2. Instale as dependências:
```sh
pip install -r requirements.txt
```
3. Inicie a aplicação:
```sh
python run.py
```
#### A API estará disponível em http://localhost:3000.

### Comandos
```sh
# Roda os testes unitários
pytest -s -v caminho_do_ficheiro/nome_do_ficheiro_test.py
```
## Documentação
A documentação foi gerada com o Swagger e se encontra em http://localhost:3000/docs.

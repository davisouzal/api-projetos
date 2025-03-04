# API de projeto

## Descrição

Este projeto é uma API para gerenciamento de projetos, permitindo a criação, edição, listagem, ativação, inativação e exclusão de projetos. A API segue boas práticas de desenvolvimento e inclui documentação tanto interativa, via Swagger, quanto pelo redoc.

## Tecnologias Utilizadas

- **Python** - Linguagem principal do projeto <br>
- **Django Rest Framework (DRF)** - Framework para criação de APIs RESTful <br>
- **PostgreSQL** - Banco de dados utilizado <br>
- **Docker** - Para facilitar a execução do ambiente<br>

## Instalação
#### Clone o repositório

```
git clone https://github.com/davisouzal/api-projetos
cd api-projetos
```

#### Crie um ambiente virtual e ative-o

```
python -m venv venv  
source venv/bin/activate   # No Windows: venv\Scripts\activate
```

#### Instale as dependências

```
pip install -r requirements.txt
```

#### Rode o docker e faça o build do container com o banco de dados

```
docker-compose up -d
// a flag d faz com que não fique mostrando o terminal do docker em seu terminal local
```
> Obs: Se estiver rodando no windows, o Docker Desktop tem que estar rodando já

#### Execute as migrações

```
python manage.py migrate
```

#### Inicie o servidor

```
python manage.py runserver
```

## Uso

A API pode ser acessada localmente via http://127.0.0.1:8000/.

Para visualizar a documentação interativa (Swagger), acesse:
http://127.0.0.1:8000/swagger/

Para acessar a documentação no formato Redoc:
http://127.0.0.1:8000/redoc/

## Contato

Agora é só aproveitar! Qualquer dúvida, entrar em contato pelo [meu GitHub](https://github.com/davisouzal)! 

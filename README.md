
# AUTH API

API de login e cadastro com autenticação JWT.

## Funcionalidades

- Criação de um novo usuario
- Login de um usuario existente
- Autenticação com JWT

## Documentação
#### Cria um novo usuario

```http
  POST /user/register
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `username` | `string` | **Obrigatório** username do usuario |
| `password` | `string` | **Obrigatório** senha do usuario |

```http
  POST /user/login
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `username` | `string` | **Obrigatório** username do usuario |
| `password` | `string` | **Obrigatório** senha do usuario |


## Execução do projeto
Para rodar esse projeto, você vai precisar executar o seguinte comando para adicionar as variáveis de ambiente no seu .env:

`pip install -r requirements.txt`

comando para fazer a migração das alterações feitas: alembic revision --autogenerate -m ""
comando para executar o projeto: uvicorn app.main:app --reload

### Ainda não foi realizado deploy desse projeto...
## Deploy

Para fazer o deploy desse projeto rode

```bash
  
```



# AUTH API

API onde é possivel realizar login e cadastro com autenticação JWT.

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


## Variáveis de Ambiente

Para rodar esse projeto, você vai precisar executar o seguinte comando para adicionar as variáveis de ambiente no seu .env:

`pip install -r requirements.txt`

variaveis que serão adicionadas ao executar o comando acima:

`alembic==1.14.1`
`annotated-types==0.7.0`
`anyio==4.8.0`
`click==8.1.8`
`colorama==0.4.6`
`ecdsa==0.19.0`
`fastapi==0.115.11`
`greenlet==3.1.1`
`h11==0.14.0`
`httptools==0.6.4`
`idna==3.10`
`Mako==1.3.9`
`MarkupSafe==3.0.2`
`passlib==1.7.4`
`psycopg2==2.9.10`
`psycopg2-binary==2.9.10`
`pyasn1==0.4.8`
`pydantic==2.10.6`
`pydantic_core==2.27.2`
`python-decouple==3.8`
`python-dotenv==1.0.1`
`python-jose==3.4.0`
`python-multipart==0.0.20`
`PyYAML==6.0.2`
`rsa==4.9`
`six==1.17.0`
`sniffio==1.3.1`
`SQLAlchemy==2.0.38`
`starlette==0.46.0`
`typing_extensions==4.12.2`
`uvicorn==0.34.0`
`watchfiles==1.0.4`
`websockets==15.0`



### Ainda não foi realizado deploy desse projeto...
## Deploy

Para fazer o deploy desse projeto rode

```bash
  
```


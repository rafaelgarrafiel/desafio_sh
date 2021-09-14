# Shipay Back-end Challenge
Essa aplicação foi desenvolvida de acordo com a solicitação no Teste [https://github.com/shipay-pag/backend-challenge/blob/master/README.md]

### Extensões:
- Restful: [Flask-restplus](http://flask-restplus.readthedocs.io/en/stable/)

- SQL ORM: [Flask-SQLalchemy](http://flask-sqlalchemy.pocoo.org/2.1/)

- Marshmallow: [Flask-Marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/)

## Como rodar ambiente de desenvolvimento

### Passo-a-passo

### Criação do ambiente virtual

Criando ambiente virtual:

```
$ python -m venv venv
```

Ativando ambiente virtual:

```
$ source venv/bin/activate
```

### Configurando aplicação

Configuração environment:

```
$ cp .env_example .env
```

Instalando pacotes:

```
$ make install
```

Criando banco de dados:

```
$ make init_db
```

### Rodando aplicação

Instalando pacotes:

```
$ make run
```

## Changelog

- Version 0.1.0 : Aplicação inicial

# Tutorial-REST-API-flask-sqlalchemy
Tutorial from 'REST API With Flask & SQL Alchemy' (Traversy Media) with some modifications by Marcus Mariano

---

## Introduction

Make a REST API with Flask and SQLAlchemy

- flask
- flask-sqlalchemy
- flask-marshmallow
- marshmallow-sqlalchemy 

---

## Installation

```sh

pipenv install

```
---

## How to Run

### Create db

on Ipython
```sh
from app.model import db
from app import create_app

db.create_all(app=create_app())
```

On Postman

Add product

```sh
POST
http://127.0.0.1:5000/api/v1.0/product

{
	"name": "Product 1",
	"description": "This is product one",
	"price": 350.00,
	"qty": 100
}
```
Show products

```sh
GET
http://127.0.0.1:5000/api/v1.0/product

```
Show single product

```sh
GET
http://127.0.0.1:5000/api/v1.0/product/1

```
Update product

```sh
PUT
http://127.0.0.1:5000/api/v1.0/product/2

{
	"name": "Product 2",
	"description": "This is product 2",
	"price": 250.00,
	"qty": 20
}

```
Delete product

```sh
DELETE
http://127.0.0.1:5000/api/v1.0/product/2

```

---

## License

Code and documentation are available according to the GNU GENERAL PUBLIC LICENSE Version 3 (see [LICENSE](https://www.gnu.org/licenses/gpl.html)).

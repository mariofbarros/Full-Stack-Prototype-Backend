# Coffee Shop Order API

A RESTful API built with **Flask** and **SQLAlchemy** to manage coffee shop orders. It supports CRUD operations for orders, includes input validation, and provides interactive API documentation via **Swagger/OpenAPI**. This backend connects directly to the [Full Stack Prototype Frontend](https://github.com/mariofbarros/Full-Stack-Prototype-Frontend).

## Features

- **CRUD Operations**: Create, Read, Update, and Delete orders.
- **Validation**: Enforces content length limits (max 100 chars) and non-empty fields.
- **Database**: Uses SQLite for lightweight, zero-configuration persistence.
- **Documentation**: Auto-generated Swagger UI via `flasgger`.
- **Error Handling**: Custom JSON error responses for 400, 404, and 500 errors.

## Tech Stack

- **Language**: Python 3.x
- **Framework**: Flask 3.0.0
- **ORM**: SQLAlchemy 2.0
- **Documentation**: Flasgger (Swagger 2.0)
- **Database**: SQLite

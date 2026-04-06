[![Status: Academic Project](https://img.shields.io/badge/Status-Academic_Project-orange)]()
[![Warning: Not for Production](https://img.shields.io/badge/Warning-Not_for_Production-red)]()

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

## Prerequisites

- **Python** (Version 3.8 or higher recommended)
- **Git**
- A code editor (e.g., VS Code)

## Setup Guide

Open your terminal (Command Prompt, PowerShell, or Git Bash) and navigate to your desired directory:

```
#Create a project folder
mkdir Full-Stack-Prototype
cd Full-Stack-Prototype

# Clone the Backend
git clone https://github.com/mariofbarros/Full-Stack-Prototype-Backend.git

# Clone the Frontend
git clone https://github.com/mariofbarros/Full-Stack-Prototype-Frontend.git
```
Your directory structure should look like this:

```
Full-Stack-Prototype/
├── Full-Stack-Prototype-Backend/
│   ├── app.py
│   ├── database.py
│   ├── requirements.txt
│   └── ...
└── Full-Stack-Prototype-Frontend/
    ├── index.html
    ├── script.js
    └── styles.css
```
Navigate to the backend folder:

```
cd Full-Stack-Prototype-Backend
```

Create a virtual environment:

```
python -m venv venv
```

Activate the virtual environment:

```
venv\Scripts\activate
```

(You should see (venv) appear at the start of your command prompt)

Install dependencies:

```
pip install -r requirements.txt
```

Start the server:

```
python app.py
```
You should see output indicating the server is running on http://127.0.0.1:5000. Keep this terminal open. You can alternatively go to http://localhost:5000/apidocs/ to open up the Swagger UI and test all routes available.

Finally, you can double click the ```index.html``` located in the **Full-Stack-Prototype-Frontend** folder to access the project's SPA. Try creating a new order. It should appear in the list immediately.

## ⚠️ Disclaimer

> **Academic Project Notice**
>
> This repository contains a **university project** developed for educational purposes and as a **Proof of Concept (PoC)**. It is **not** intended for production use, commercial deployment, or handling sensitive data.
>
> **Key Limitations:**
> - **Security:** The application lacks robust security measures (e.g., authentication, authorization, input sanitization beyond basics, and secure data encryption) required for real-world environments.
> - **Scalability:** The architecture is designed for a single-user/local environment and does not support high traffic, concurrent users, or distributed systems.
> - **Features:** Several features are incomplete or simplified to focus on core learning objectives.
>
> **Future Roadmap:**
> This project is a work in progress. I intend to continue developing it to address these limitations, implement security best practices, and explore scalability solutions as part of my ongoing learning journey.
>
> **Usage:**
> Feel free to review the code for educational insights, but please do not deploy this in a live environment without significant refactoring and security auditing.

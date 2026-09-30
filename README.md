# AI Support Ticket Triage & Management System

A Python backend application that uses FastAPI and machine learning to classify customer support tickets, assign priority, and store ticket information in a SQLite database.

## Features

* **Ticket Management:** Create, view, update, and delete support tickets through REST API endpoints.
* **AI Ticket Classification:** Uses TF-IDF and Logistic Regression to classify tickets into categories such as Billing, Account, Technical, and General.
* **Priority Assignment:** Analyzes ticket information and assigns a priority level based on the issue.
* **Data Validation:** Uses Pydantic models to validate incoming API requests.
* **Database Storage:** Uses SQLAlchemy with SQLite to store and manage ticket records.
* **Interactive API Documentation:** FastAPI Swagger UI is available for testing the endpoints.

## Tech Stack

* **Python**
* **FastAPI**
* **SQLAlchemy**
* **SQLite**
* **Pydantic**
* **scikit-learn**
* **TF-IDF**
* **Logistic Regression**
* **Git & GitHub**

## How It Works

1. A user submits a support ticket through the API.
2. FastAPI validates the incoming request using Pydantic.
3. The ticket title and description are processed using TF-IDF.
4. The Logistic Regression model predicts the ticket category.
5. The application determines the ticket priority.
6. The ticket is stored in the SQLite database using SQLAlchemy.
7. The stored ticket can later be retrieved, updated, or deleted through the API.

## API Endpoints

| Method | Endpoint        | Description                         |
| ------ | --------------- | ----------------------------------- |
| GET    | `/`             | Checks whether the API is running   |
| POST   | `/tickets`      | Creates and classifies a new ticket |
| GET    | `/tickets`      | Retrieves stored tickets            |
| GET    | `/tickets/{id}` | Retrieves a specific ticket         |
| PUT    | `/tickets/{id}` | Updates an existing ticket          |
| DELETE | `/tickets/{id}` | Deletes a ticket                    |

## Project Structure

```text
AI-support-ticket-system/
│
├── main.py
├── database.py
├── models.py
├── requirements.txt
├── README.md
└── .gitignore
```

### File Overview

* `main.py` — FastAPI application, API routes, ticket classification and priority logic
* `database.py` — Database engine and SQLAlchemy session setup
* `models.py` — Database table/model definitions
* `requirements.txt` — Python dependencies
* `.gitignore` — Files and folders excluded from Git

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Varshhhaaa/AI-support-ticket-system.git
cd AI-support-ticket-system
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
uvicorn main:app --reload
```

### 5. Open Swagger UI

Visit:

```text
http://127.0.0.1:8000/docs
```

You can use Swagger UI to send requests and test the API endpoints.

## Example Ticket

### Request

```json
{
  "title": "Payment transaction failed",
  "description": "My payment went through but my premium status is still inactive."
}
```

### Example Result

```text
Category: Billing
Priority: High
Status: Open
```

## Future Improvements

* Add authentication and authorization.
* Migrate from SQLite to PostgreSQL.
* Improve the ticket classification model with a larger training dataset.
* Add automated tests for API endpoints and classification logic.
* Add a frontend dashboard for viewing and managing tickets.

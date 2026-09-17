# AI Support Ticket Triage & Management System

A backend system that automatically analyzes customer support tickets, classifies them into categories, assigns priority, and provides REST APIs to manage tickets.

## Features

* Create, view, update, and delete support tickets
* Automatically classify tickets using Machine Learning
* Categorize tickets into:

  * Billing
  * Account
  * Technical
* Automatically assign ticket priority
* Store ticket data using SQLite
* REST APIs built with FastAPI
* Interactive API documentation using Swagger UI

## Tech Stack

* **Python**
* **FastAPI**
* **SQLAlchemy**
* **SQLite**
* **Pydantic**
* **scikit-learn**
* **TF-IDF**
* **Logistic Regression**

## How It Works

1. A user submits a support ticket through the API.
2. The ticket title and description are analyzed.
3. TF-IDF converts the text into numerical features.
4. A Logistic Regression model predicts the ticket category.
5. The system assigns a priority based on the ticket content.
6. The ticket is stored in the SQLite database.

## API Endpoints

| Method | Endpoint               | Description                 |
| ------ | ---------------------- | --------------------------- |
| GET    | `/`                    | Check if the API is running |
| GET    | `/tickets`             | Get all tickets             |
| GET    | `/tickets/{ticket_id}` | Get a specific ticket       |
| POST   | `/tickets`             | Create a new ticket         |
| PUT    | `/tickets/{ticket_id}` | Update a ticket             |
| DELETE | `/tickets/{ticket_id}` | Delete a ticket             |

## Project Structure

```text
ai-support-ticket-system/
│
├── main.py
├── database.py
├── models.py
├── requirements.txt
├── README.md
├── .gitignore
└── venv/
```

## How to Run

Clone the repository:

```bash
git clone https://github.com/Varshhhaaaa/AI-support-ticket-system.git
cd AI-support-ticket-system
```

Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Start the FastAPI server:

```bash
python -m uvicorn main:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## Example

A ticket such as:

> **Title:** Payment failed
> **Description:** Money was deducted but my order was not placed.

can be automatically classified as:

* **Category:** Billing
* **Priority:** High

## Future Improvements

* Add authentication and authorization
* Add a frontend dashboard
* Improve the ML model with a larger real-world dataset
* Add ticket search and filtering
* Deploy the application to the cloud

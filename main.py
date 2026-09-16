from fastapi import FastAPI
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from openai import OpenAI
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

app = FastAPI()

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# SQLite database
DATABASE_URL = "sqlite:///./tickets_ai.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


# Database table
class TicketDB(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    status = Column(String, default="Open")
    category = Column(String)
    priority = Column(String)


Base.metadata.create_all(bind=engine)


# Data accepted from API
class Ticket(BaseModel):
    title: str
    description: str


@app.get("/")
def home():
    return {"message": "AI Support Ticket System is running!"}


# Local fallback triage
# Simple ML model for ticket category
training_texts = [
    "payment failed",
    "money deducted",
    "refund not received",
    "charged for order",
    "cannot login",
    "forgot password",
    "account locked",
    "website crashing",
    "application error",
    "system bug",
    "feature not working",
]

training_labels = [
    "Billing",
    "Billing",
    "Billing",
    "Billing",
    "Account",
    "Account",
    "Account",
    "Technical",
    "Technical",
    "Technical",
    "Technical",
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(training_texts)

model = LogisticRegression()
model.fit(X, training_labels)


def triage_ticket(title: str, description: str):
    text = title + " " + description

    features = vectorizer.transform([text])
    category = model.predict(features)[0]

    if "urgent" in text.lower() or "failed" in text.lower():
        priority = "High"
    else:
        priority = "Medium"

    return category, priority


@app.get("/tickets")
def get_tickets():
    db = SessionLocal()
    tickets = db.query(TicketDB).all()
    db.close()
    return tickets


@app.get("/tickets/{ticket_id}")
def get_ticket(ticket_id: int):
    db = SessionLocal()
    ticket = db.query(TicketDB).filter(TicketDB.id == ticket_id).first()
    db.close()

    if ticket is None:
        return {"message": "Ticket not found"}

    return ticket


@app.post("/tickets")
def create_ticket(ticket: Ticket):
    db = SessionLocal()

    category, priority = triage_ticket(
        ticket.title,
        ticket.description
    )

    new_ticket = TicketDB(
        title=ticket.title,
        description=ticket.description,
        category=category,
        priority=priority
    )

    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    db.close()

    return new_ticket


@app.put("/tickets/{ticket_id}")
def update_ticket(ticket_id: int, status: str):
    db = SessionLocal()

    ticket = db.query(TicketDB).filter(
        TicketDB.id == ticket_id
    ).first()

    if ticket is None:
        db.close()
        return {"message": "Ticket not found"}

    ticket.status = status
    db.commit()
    db.refresh(ticket)
    db.close()

    return ticket


@app.delete("/tickets/{ticket_id}")
def delete_ticket(ticket_id: int):
    db = SessionLocal()

    ticket = db.query(TicketDB).filter(
        TicketDB.id == ticket_id
    ).first()

    if ticket is None:
        db.close()
        return {"message": "Ticket not found"}

    db.delete(ticket)
    db.commit()
    db.close()

    return {"message": "Ticket deleted successfully"}
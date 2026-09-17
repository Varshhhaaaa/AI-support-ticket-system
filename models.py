from sqlalchemy import Column, Integer, String
from database import Base


class TicketDB(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    status = Column(String, default="Open")
    category = Column(String)
    priority = Column(String)
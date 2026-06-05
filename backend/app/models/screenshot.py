from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from ..database import Base

class Screenshot(Base):
    __tablename__ = "screenshots"

    id = Column(Integer, primary_key=True, index=True)
    visitor_id = Column(Integer, ForeignKey("visitors.id"))
    session_id = Column(String(100))
    url = Column(String(500))
    screenshot_path = Column(String(500))
    timestamp = Column(DateTime, server_default=func.now())
    notes = Column(String(500), nullable=True)

    def __repr__(self):
        return f"<Screenshot(id={self.id}, visitor_id={self.visitor_id})>"

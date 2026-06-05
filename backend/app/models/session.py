from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from ..database import Base
from datetime import datetime

class Session(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, index=True)
    visitor_id = Column(Integer, ForeignKey("visitors.id"))
    session_id = Column(String(100), unique=True, index=True)
    start_time = Column(DateTime, default=datetime.utcnow)
    end_time = Column(DateTime, nullable=True)
    page_views = Column(Integer, default=1)
    clicks = Column(Integer, default=0)
    hovers = Column(Integer, default=0)
    path = Column(Text)  # JSON string of navigation path
    events = relationship("Event", back_populates="session")
    visitor = relationship("Visitor")

    def __repr__(self):
        return f"<Session(id={self.id}, visitor_id={self.visitor_id})>"

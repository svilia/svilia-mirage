from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.sql import func
from ..database import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String(100), ForeignKey("sessions.session_id"))
    visitor_id = Column(Integer, ForeignKey("visitors.id"))
    event_type = Column(String(50))  # click, hover, scroll, etc.
    element = Column(String(200))
    coordinates = Column(String(100))  # x,y
    timestamp = Column(DateTime, server_default=func.now())
    metadata = Column(Text)  # JSON string for additional data

    session = relationship("Session", back_populates="events")

    def __repr__(self):
        return f"<Event(id={self.id}, type={self.event_type})>"

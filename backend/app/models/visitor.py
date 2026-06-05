from sqlalchemy import Column, Integer, String, DateTime, Float, Text
from sqlalchemy.sql import func
from ..database import Base
from datetime import datetime

class Visitor(Base):
    __tablename__ = "visitors"

    id = Column(Integer, primary_key=True, index=True)
    tracking_id = Column(String(100), unique=True, index=True)
    ip_address = Column(String(50))
    asn = Column(String(100))
    country = Column(String(100))
    city = Column(String(100))
    timezone = Column(String(100))
    user_agent = Column(Text)
    browser = Column(String(100))
    os = Column(String(100))
    device = Column(String(100))
    language = Column(String(50))
    screen_width = Column(Integer)
    screen_height = Column(Integer)
    referrer = Column(Text)
    timestamp = Column(DateTime, server_default=func.now())
    session_duration = Column(Float, default=0.0)
    revisit_count = Column(Integer, default=1)
    
    def __repr__(self):
        return f"<Visitor(id={self.id}, ip={self.ip_address}, country={self.country})>"

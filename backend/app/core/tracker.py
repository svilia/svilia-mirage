from user_agents import parse as ua_parse
import json
from datetime import datetime
from ..models.visitor import Visitor
from ..models.session import Session
from ..models.event import Event
from .logger import logger

class Tracker:
    @staticmethod
    def parse_user_agent(user_agent: str):
        ua = ua_parse(user_agent)
        return {
            "browser": ua.browser.family,
            "os": ua.os.family,
            "device": ua.device.family
        }
    
    @staticmethod
    def create_tracking_id():
        import uuid
        return str(uuid.uuid4())
    
    @staticmethod
    def log_visitor(db, visitor_data: dict):
        tracking_id = Tracker.create_tracking_id()
        
        visitor = Visitor(
            tracking_id=tracking_id,
            ip_address=visitor_data.get("ip"),
            asn=visitor_data.get("asn"),
            country=visitor_data.get("country"),
            city=visitor_data.get("city"),
            timezone=visitor_data.get("timezone"),
            user_agent=visitor_data.get("user_agent"),
            browser=visitor_data.get("browser"),
            os=visitor_data.get("os"),
            device=visitor_data.get("device"),
            language=visitor_data.get("language"),
            screen_width=visitor_data.get("screen_width"),
            screen_height=visitor_data.get("screen_height"),
            referrer=visitor_data.get("referrer")
        )
        
        db.add(visitor)
        db.commit()
        db.refresh(visitor)
        logger.info(f"New visitor logged: {visitor.ip_address} from {visitor.country}")
        return visitor
    
    @staticmethod
    def log_session(db, visitor_id: int, session_data: dict):
        session = Session(
            visitor_id=visitor_id,
            session_id=session_data.get("session_id"),
            path=json.dumps(session_data.get("path", []))
        )
        db.add(session)
        db.commit()
        db.refresh(session)
        return session

    @staticmethod
    def log_event(db, session_id: str, event_data: dict):
        """Log behavioral events like clicks, hovers."""
        event = Event(
            session_id=session_id,
            event_type=event_data.get("type", "unknown"),
            element=event_data.get("element"),
            coordinates=event_data.get("coordinates"),
            metadata=json.dumps(event_data.get("metadata", {}))
        )
        db.add(event)
        db.commit()
        db.refresh(event)
        logger.info(f"Event logged: {event.event_type} for session {session_id}")
        return event

    @staticmethod
    def update_session_duration(db, session_id: str, duration: float):
        """Update session duration for behavioral analysis."""
        session = db.query(Session).filter(Session.session_id == session_id).first()
        if session:
            session.session_duration = (session.session_duration or 0) + duration
            db.commit()
            logger.info(f"Session duration updated for {session_id}: {duration}s")


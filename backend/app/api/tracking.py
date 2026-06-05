from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..core.tracker import Tracker
from ..core.geoip import GeoIPService
from ..core.fingerprint import generate_fingerprint
from ..config import settings
import json

router = APIRouter()

geoip = GeoIPService(settings.GEOIP_DB_PATH)

@router.post("/track")
async def track_visitor(request: Request, db: Session = Depends(get_db)):
    try:
        client_ip = request.client.host if request.client else "127.0.0.1"
        user_agent = request.headers.get("user-agent", "")
        referrer = request.headers.get("referer", "")
        language = request.headers.get("accept-language", "")
        
        # Get body for additional data
        body = await request.json() if request.headers.get("content-type") == "application/json" else {}
        
        ua_info = Tracker.parse_user_agent(user_agent)
        
        geo_info = geoip.get_location(client_ip)
        
        visitor_data = {
            "ip": client_ip,
            "user_agent": user_agent,
            "referrer": referrer,
            "language": language,
            "browser": ua_info["browser"],
            "os": ua_info["os"],
            "device": ua_info["device"],
            "screen_width": body.get("screen_width"),
            "screen_height": body.get("screen_height"),
            "timezone": body.get("timezone"),
            **geo_info
        }
        
        visitor = Tracker.log_visitor(db, visitor_data)
        
        fingerprint = generate_fingerprint(visitor_data)
        
        return {
            "tracking_id": visitor.tracking_id,
            "fingerprint": fingerprint,
            "message": "Visitor tracked successfully"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/event")
async def log_event(request: Request, db: Session = Depends(get_db)):
    """Log client-side behavioral events."""
    try:
        data = await request.json()
        session_id = data.get("session_id")
        event_type = data.get("event_type")
        
        if not session_id:
            raise HTTPException(status_code=400, detail="session_id required")
        
        Tracker.log_event(db, session_id, {
            "type": event_type,
            "element": data.get("element"),
            "coordinates": data.get("coordinates"),
            "metadata": data.get("metadata", {})
        })
        
        # Broadcast via websocket if needed
        return {"status": "success", "event": event_type}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/bait/{bait_type}")
async def serve_bait_page(bait_type: str):
    """Serve bait templates for testing."""
    # In production, use templates.render
    return {"bait": f"Template for {bait_type} ready for deployment"}


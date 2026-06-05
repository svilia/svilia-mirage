from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.visitor import Visitor
from ..models.session import Session
from ..models.event import Event

router = APIRouter()

@router.get("/")
async def get_sessions(db: Session = Depends(get_db), limit: int = 50):
    sessions = db.query(Session).order_by(Session.start_time.desc()).limit(limit).all()
    return {"sessions": sessions}

@router.get("/{session_id}")
async def get_session(session_id: str, db: Session = Depends(get_db)):
    session = db.query(Session).filter(Session.session_id == session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    return session

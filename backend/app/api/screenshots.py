from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.screenshot import Screenshot

router = APIRouter()

@router.get("/")
async def get_screenshots(db: Session = Depends(get_db)):
    screenshots = db.query(Screenshot).all()
    return {"screenshots": screenshots}

# TODO: Implement screenshot capture with Playwright

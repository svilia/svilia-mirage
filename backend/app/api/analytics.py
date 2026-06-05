from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.visitor import Visitor

router = APIRouter()

@router.get("/stats")
async def get_stats(db: Session = Depends(get_db)):
    total_visitors = db.query(Visitor).count()
    countries = db.query(Visitor.country).distinct().all()
    return {
        "total_visitors": total_visitors,
        "unique_countries": len(countries)
    }

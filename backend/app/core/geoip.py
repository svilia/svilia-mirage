import geoip2.database
from pathlib import Path
from .logger import logger

class GeoIPService:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.reader = None
        try:
            if Path(db_path).exists():
                self.reader = geoip2.database.Reader(db_path)
                logger.info("GeoIP database loaded successfully")
            else:
                logger.warning(f"GeoIP database not found at {db_path}")
        except Exception as e:
            logger.error(f"Failed to load GeoIP: {e}")
    
    def get_location(self, ip: str):
        if not self.reader:
            return {"country": "Unknown", "city": "Unknown", "timezone": "UTC"}
        
        try:
            response = self.reader.city(ip)
            return {
                "country": response.country.name or "Unknown",
                "city": response.city.name or "Unknown",
                "timezone": response.location.time_zone or "UTC",
                "asn": getattr(response, 'autonomous_system_organization', 'Unknown')
            }
        except Exception:
            return {"country": "Unknown", "city": "Unknown", "timezone": "UTC", "asn": "Unknown"}

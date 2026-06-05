import hashlib
import json

def generate_fingerprint(data: dict) -> str:
    """Generate a simple browser fingerprint hash."""
    fingerprint_data = {
        "user_agent": data.get("user_agent"),
        "language": data.get("language"),
        "screen": f"{data.get('screen_width')}x{data.get('screen_height')}",
        "timezone": data.get("timezone")
    }
    fingerprint_str = json.dumps(fingerprint_data, sort_keys=True)
    return hashlib.md5(fingerprint_str.encode()).hexdigest()

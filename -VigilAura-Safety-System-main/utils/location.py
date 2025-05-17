# utils/location.py

# This will be called when sending alert
_location_data = {"lat": 0.0, "lon": 0.0}

def save_location(lat, lon):
    global _location_data
    _location_data = {"lat": lat, "lon": lon}
    print(f"📍 Location saved: {lat}, {lon}")

def get_location():
    return _location_data

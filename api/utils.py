def validate_coordinates(coordinates: str) -> bool:
    try:
        lat, lon = map(float, coordinates.split(','))
        return -90 <= lat <= 90 and -180 <= lon <= 180
    except ValueError:
        return False

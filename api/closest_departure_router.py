import logging

from fastapi import HTTPException, APIRouter

from api.utils import validate_coordinates
from database_logic.get_closest_departure import fetch_departures_from_db

router = APIRouter()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_closest_departures(city: str, start_coordinates: str, end_coordinates: str, start_time: str, limit: int):
    if city.lower() != "wroclaw":
        raise HTTPException(status_code=400, detail="Currently, only 'Wroclaw' is supported.")

    if not validate_coordinates(start_coordinates) or not validate_coordinates(end_coordinates):
        raise HTTPException(status_code=400, detail="Invalid coordinates format.")

    departures = fetch_departures_from_db(city, start_coordinates, end_coordinates, start_time, limit)

    return {
        "metadata": {
            "self": f"/public_transport/city/{city}/closest_deparures?start_coordinates={start_coordinates}&end_coordinates={end_coordinates}&start_time={start_time}&limit={limit}",
            "city": city,
            "query_parameters": {
                "start_coordinates": start_coordinates,
                "end_coordinates": end_coordinates,
                "start_time": start_time,
                "limit": limit
            }
        },
        "departures": departures
    }


@router.get("/public_transport/city/{city}/closest_departures")
def closest_departures(city: str, start_coordinates: str, end_coordinates: str, start_time: str, limit: int):
    logger.info(
        f"Received request for closest departures in {city} with start_coordinates={start_coordinates}, end_coordinates={end_coordinates}, start_time={start_time}, limit={limit}")
    return get_closest_departures(city, start_coordinates, end_coordinates, start_time, limit)

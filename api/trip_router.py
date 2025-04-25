import logging

from fastapi import APIRouter, HTTPException

from database_logic.fetch_trip_details import fetch_trip_details_from_db

router = APIRouter()

logger = logging.getLogger(__name__)


def get_trip_details(city: str, trip_id: str):
    if city.lower() != "wroclaw":
        raise HTTPException(status_code=400, detail="Currently, only 'Wroclaw' is supported.")

    trip_details = fetch_trip_details_from_db(city, trip_id)

    return {
        "metadata": {
            "self": f"/public_transport/city/{city}/trip/{trip_id}",
            "city": city,
            "query_parameters": {
                "trip_id": trip_id
            }
        },
        "trip_details": trip_details
    }


@router.get("/public_transport/city/{city}/trip/{trip_id}")
def trip_details(city: str, trip_id: str):
    logger.info(f"Received request for trip details in {city} with trip_id={trip_id}")

    return get_trip_details(city, trip_id)

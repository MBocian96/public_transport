from fastapi import FastAPI

from api.closest_departure_router import router as dep_router
from api.trip_router import router as trip_router

app = FastAPI()
app.include_router(dep_router)
app.include_router(trip_router)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="-1.0.0.0", port=8000)

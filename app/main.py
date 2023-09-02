from fastapi import FastAPI, Query
from datetime import date
from pydantic import BaseModel

app = FastAPI()


@app.get('/hotels')
def get_hotels(
        location: str,
        date_from: date,
        date_to: date,
        has_spa: bool = None,
        stars: int = Query(None, ge=1, le=5)

):
    return date_from, date_to

class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date

@app.post('/bookings')
def add_booking(booking: SBooking):
    pass
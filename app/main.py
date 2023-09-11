from fastapi import FastAPI, Query
from datetime import date
from pydantic import BaseModel

from app.bookings.router import router as router_bookings
from app.users.router import router_users


app = FastAPI()

app.include_router(router_users)
app.include_router(router_bookings)


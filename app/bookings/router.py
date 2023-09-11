from fastapi import APIRouter, Depends
from fastapi import Request

from app.bookings.dao import BookingDAO
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix='/bookings',
    tags=['Bookings']
)


@router.get('')
async def get_bookings(user: Users = Depends(get_current_user)):  # ->list[SBooking]
    return await BookingDAO.find_all(user_id=user.id)


@router.get('/{booking_id}')
async def get_bookings(booking_id: int):
    return await BookingDAO.find_by_id(booking_id)

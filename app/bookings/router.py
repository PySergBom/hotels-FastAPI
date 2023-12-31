from datetime import date

from fastapi import APIRouter, Depends, HTTPException

from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking
from app.exceptions import RoomCannotBeBooked, UserDoesNotHaveAccessRightsException
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix='/bookings',
    tags=['Bookings']
)


@router.get('')
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SBooking]:
    return await BookingDAO.find_all(user_id=user.id)


@router.get('/{booking_id}',)
async def get_bookings(
        booking_id: int,
        user: Users = Depends(get_current_user),
) -> SBooking:
    booking = await BookingDAO.find_by_id(booking_id)
    if not booking:
        raise HTTPException(status_code=404)
    if booking.user_id != user.id:
        raise UserDoesNotHaveAccessRightsException
    return booking


@router.post('')
async def add_booking(
        room_id: int, date_from: date, date_to: date,
        user: Users = Depends(get_current_user),
):
    booking = await BookingDAO.add(user.id, room_id, date_from, date_to)
    if not booking:
        raise RoomCannotBeBooked


@router.delete('/{booking_id}')
async def delete_booking(
        booking_id: int,
        user: Users = Depends(get_current_user),
):
    current_user = user
    return await BookingDAO.delete(id=booking_id, user_id=current_user.id)

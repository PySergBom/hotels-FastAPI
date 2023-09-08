from fastapi import APIRouter

from app.bookings.dao import BookingDAO

router = APIRouter(
    prefix='/bookings',
    tags=['Bookings']
)


@router.get('')
async def get_bookings():
    return await BookingDAO.find_all()


# @router.get('/{booking_id}')
# async def get_bookings(booking_id: int):
#     return await BookingDAO.find_by_id(booking_id)


@router.get('/filter')
async def get_bookings(room_id: int = None):
    return await BookingDAO.get_one_or_none(room_id=room_id)

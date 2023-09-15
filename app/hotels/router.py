from datetime import date
from typing import List

from fastapi import APIRouter

from app.hotels.dao import HotelDAO
from app.hotels.schemas import SHotel

router = APIRouter(
    prefix='/hotels',
    tags=['Hotels']
)


@router.get('')
async def get_hotels() -> List[SHotel]:
    return await HotelDAO.find_all()


@router.get('/{location}')
async def get_left_rooms_in_hotels_with_filter(
        location: str,
        date_from: date,
        date_to: date,
) -> List[SHotel]:
    return await HotelDAO.find_left(location, date_from, date_to)


from datetime import date
from typing import List

from fastapi import APIRouter

from app.hotels.rooms.dao import RoomDAO
from app.hotels.rooms.schemas import SRoom, SRoomInfo

router = APIRouter(
    prefix='/hotels',
    tags=['Hotels']
)


@router.get('/rooms')
async def get_rooms() -> List[SRoom]:
    return await RoomDAO.find_all()


@router.get("/{hotel_id}/rooms")
async def get_rooms_by_time(
        hotel_id: int,
        date_from: date,
        date_to: date
) -> SRoomInfo:
    rooms = await RoomDAO.find_all(hotel_id, date_from, date_to)
    return rooms

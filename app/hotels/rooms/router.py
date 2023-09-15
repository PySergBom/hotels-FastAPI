from typing import List

from fastapi import APIRouter

from app.hotels.rooms.dao import RoomDAO
from app.hotels.rooms.schemas import SRoom

router = APIRouter(
    prefix='/hotels',
    tags=['Hotels']
)


@router.get('/rooms')
async def get_rooms() -> List[SRoom]:
    return await RoomDAO.find_all()

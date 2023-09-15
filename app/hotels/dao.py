from datetime import date

from sqlalchemy import select

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.hotels.models import Hotels


class HotelDAO(BaseDAO):
    model = Hotels

    @classmethod
    async def find_left(
            cls,
            location: str,
            date_from: date,
            date_to: date,
            **filter_by
    ):

        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter_by).where(
                Hotels.location.like(f'%{location}%')
            )
            result = await session.execute(query)
            return result.mappings().all()

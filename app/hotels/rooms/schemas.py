from typing import List

from pydantic import BaseModel


class SRoom(BaseModel):
    id: int
    hotel_id: int
    name: str
    description: str
    price: int
    services: List[str]
    image_id: int

    class Config:
        orm_mode = True

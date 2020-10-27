from uuid import UUID, uuid4
from typing import List

from models.parking_strategy import ParkingStrategy


class ParkingLot:
    lot_id: UUID
    name: str

    def __init__(self, name: str, parking_strategy: ParkingStrategy):
        self.lot_id = uuid4()
        self.name = name
        self.parking_strategy = parking_strategy

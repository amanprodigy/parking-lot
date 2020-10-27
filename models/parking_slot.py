from uuid import UUID, uuid4
from models.parking_lot import ParkingLot
from models.slot_type import SlotType


class ParkingSlot:
    '''
    Represents a single slot in the parking area
    '''
    slot_id: UUID
    parking_lot: ParkingLot
    slot_type: SlotType
    slot_number: str
    occupied: bool

    def __init__(self, parking_lot: ParkingLot, slot_type: SlotType,
                 slot_number: str):
        self.slot_id = uuid4()
        self.parking_lot = parking_lot
        self.slot_type = slot_type
        self.slot_number = slot_number
        self.occupied = False

    def getSlotNumber(self):
        return self.slot_number

    def __str__(self):
        return f"{self.parking_lot} - {self.slot_type} - {self.slot_number}"

    def __repr__(self):
        return f"{self.parking_lot} - {self.slot_type} - {self.slot_number}"

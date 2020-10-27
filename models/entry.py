from models.parking_slot import ParkingSlot
from models.vehicle import Vehicle
from datetime import datetime


class ParkEntry:
    slot: ParkingSlot
    vehicle: Vehicle
    entry_time: datetime
    exit_time: datetime

    def __init__(self, slot: ParkingSlot, vehicle: Vehicle):
        self.slot = slot
        self.vehicle = vehicle
        self.entry_time = datetime.now()

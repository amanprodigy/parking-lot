from db import slots, lots, vehicles, entries
from config import ALLOWED_TYPE

from models.parking_lot import ParkingLot
from models.vehicle import Vehicle
from models.parking_strategy import ParkingStrategy
from models.parking_slot import ParkingSlot
from models.slot_type import SlotType
from models.vehicle_type import VehicleType
from models.entry import ParkEntry
from errors import SlotNotAvailableException


class ParkingService:
    @staticmethod
    def add_slot(parking_lot: ParkingLot, slot_type: SlotType, slot_number: str):
        new_slot = ParkingSlot(parking_lot, slot_type, slot_number)
        slots.append(new_slot)

    @staticmethod
    def add_vehicle(number: str, vehicle_type: VehicleType):
        new_vehicle = Vehicle(number, vehicle_type)
        vehicles.append(new_vehicle)
        return new_vehicle

    @staticmethod
    def assign_slot(
        parking_lot: ParkingLot, vehicle: Vehicle, parking_strategy: ParkingStrategy
    ):
        # Transaction in db
        for slot in slots:
            slot_type = slot.slot_type.value
            allowed_types = ALLOWED_TYPE[slot_type]
            if vehicle.vehicle_type in allowed_types and slot.occupied is False:
                slot.occupied = True
                entry = ParkEntry(slot, vehicle)
                entries.append(entry)
                return entry
        raise SlotNotAvailableException()

    @staticmethod
    def exit_vehicle(self, parking_slot: ParkingSlot):
        pass

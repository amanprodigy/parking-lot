from config import APP_NAME
from db import lots, entries
from models.parking_lot import ParkingLot
from models.parking_strategy import ParkingStrategy
from models.slot_type import SlotType
from models.vehicle_type import VehicleType
from services.parking_service import ParkingService

print('Starting Parking Lot Demo')

imagine = ParkingLot('Imagine Parking', ParkingStrategy.NATURAL_NUMBER)
lots.append(imagine)

ParkingService.add_slot(imagine, SlotType.LARGE, '001')
# ParkingService.add_slot(imagine, SlotType.MEDIUM, '002')
# ParkingService.add_slot(imagine, SlotType.SMALL, '003')
# ParkingService.add_slot(imagine, SlotType.LARGE, '004')
# ParkingService.add_slot(imagine, SlotType.XLARGE, '005')
# ParkingService.add_slot(imagine, SlotType.SMALL, '006')
# ParkingService.add_slot(imagine, SlotType.XLARGE, '007')
# ParkingService.add_slot(imagine, SlotType.SMALL, '008')

swift = ParkingService.add_vehicle('ABC123', VehicleType.HATCHBACK)
print(swift)
duke = ParkingService.add_vehicle('XYZ321', VehicleType.TWO_WHEELER)
# ecosport = ParkingService.add_vehicle('ZZRE433', VehicleType.SUV)
entry1 = ParkingService.assign_slot(imagine, duke,
                                    ParkingStrategy.NATURAL_NUMBER)
print(entry1)

# entry2 = ParkingService.assign_slot(imagine, duke,
#                                     ParkingStrategy.NATURAL_NUMBER)
# print(entry2)
print(entries)

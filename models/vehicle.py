from models.vehicle_type import VehicleType
from config import VEHICLE_TYPE_HOURLY_RATE


class Vehicle:
    """
    Represents the vechicle
    """

    def __init__(self, vehicle_number: str, vehicle_type: VehicleType):
        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type

    def getVehicleNumber(self):
        return self.vehicle_number

    def getVehicleType(self):
        return self.vehicle_type

    def getHourlyRate(self):
        return VEHICLE_TYPE_HOURLY_RATE[self.vehicle_type]

    def __str__(self):
        return f"{self.vehicle_type} - {self.vehicle_number}"

    def __repr__(self):
        return f"{self.vehicle_type} - {self.vehicle_number}"

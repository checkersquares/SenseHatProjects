from enum import Enum

class MeasureType(Enum):
    Accelerometer = 0
    Gyroscope = 1
    Magnetometer = 2
    Temperature = 3
    Pressure = 4
    Humidity = 5
    Color = 6

class Measurement():
    def __init__(self, sensor): 
        self.Sensor = sensor
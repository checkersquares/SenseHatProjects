from enum import Enum
import datetime

class MeasureType(Enum):
    Accelerometer = 0
    Gyroscope = 1
    Magnetometer = 2
    Thermometer = 3
    Barometer = 4
    Humidity = 5
    Color = 6

class Measurement():
    def __init__(self, sensor): 
        self.Sensor = sensor
        self.Timestamp = datetime.datetime.now()
        self.Data = {}
    def getData(self):
        return self.Data
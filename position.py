from enum import Enum
import measurement

class MeasureType(Enum):
    Accelerometer = 0
    Gyroscope = 1
    Magnetometer = 2

class Position(measurement.Measurement):
    def __init__(self, x, y, z, sensor = MeasureType.Gyroscope):
        self.Sensor = str(sensor.name)
        self.X = x
        self.Y = y
        self.Z = z
    def change(self, x, y, z):
        res = {}
        res["DeltaX"] = self.X - x
        res["DeltaY"] = self.Y - y
        res["DeltaZ"] = self.Z - z
        self.X = x
        self.Y = y
        self.Z = z
        return res
    def getPosition(self):
        res = {}
        res["X"] = self.X
        res["Y"] = self.Y
        res["Z"] = self.Z
        return res
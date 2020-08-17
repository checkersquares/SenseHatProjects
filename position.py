from enum import Enum
import measurement

class MeasureType(Enum):
    Accelerometer = 0
    Gyroscope = 1
    Magnetometer = 2

class Position(measurement.Measurement):
    def __init__(self, x, y, z, measureType = MeasureType.Gyroscope):
        super().__init__(measureType.name)
        self.setPosition(x, y, z)
    def change(self, x, y, z):
        res = {}
        res["DeltaX"] = self.Data["X"] + x
        res["DeltaY"] = self.Data["Y"] + y
        res["DeltaZ"] = self.Data["Z"] + z
        self.Data["X"] = x
        self.Data["Y"] = y
        self.Data["Z"] = z
        return res
    def setPosition(self, x, y, z):
        self.Data["X"] = x
        self.Data["Y"] = y
        self.Data["Z"] = z
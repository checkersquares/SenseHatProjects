from enum import Enum
import measurement

class TempSystem(Enum):
    Kelvin = 0
    Celsius = 1
    Farenheit = 2

class Temperature(measurement.Measurement):
    def __init__(self, value, system = TempSystem.Kelvin, precision=2):
        super().__init__("Temperature")
        self.System = system
        self.setTemp(value, system)
    def toKelvin(self, value, precision):
        res = 0.0
        p = pow(10, precision)
        if self.System == TempSystem.Kelvin:
            res =  value
        elif self.System == TempSystem.Celsius:
            res = value + 273.15
        elif self.System == TempSystem.Farenheit:
            res = ((value - 32) / 1.8) + 273.15
        return round(res * p) / p
    def toCelsius(self, value, precision):
        res = 0.0
        p = pow(10, precision)
        if self.System == TempSystem.Kelvin:
            res = value - 273.15
        elif self.System == TempSystem.Celsius:
            res = value
        elif self.System == TempSystem.Farenheit:
            res = ((value - 32) / 1.8)
        return round(res * p) / p
    def toFahrenheit(self, value, precision):
        res = 0.0
        p = pow(10, precision)
        if self.System == TempSystem.Kelvin:
            res = ((value - 273.15) * 1.8) + 32
        elif self.System == TempSystem.Celsius:
            res = (value * 1.8) + 32
        elif self.System == TempSystem.Farenheit:
            res = value
        return round(res * p) / p
    def setTemp(self, value, system = TempSystem.Kelvin, precision = 2):
        self.System = system
        self.Data["K"] = self.toKelvin(value, precision)
        self.Data["C"] = self.toCelsius(value, precision)
        self.Data["F"] = self.toFahrenheit(value, precision)
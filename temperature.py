from enum import Enum

class TempSystem(Enum):
    Kelvin = 0
    Celsius = 1
    Farenheit = 2

class Temperature():
    def __init__(self, value, system = TempSystem.Kelvin, precision=2):
        self.Value = value
        self.System = system
        self.Precision = pow(10, precision)
    def toKelvin(self):
        res = 0.0
        if self.System == TempSystem.Kelvin:
            res =  self.Value
        elif self.System == TempSystem.Celsius:
            res = self.Value + 273.15
        elif self.System == TempSystem.Farenheit:
            res = ((self.Value - 32) / 1.8) + 273.15
        return round(res * self.Precision) / self.Precision
    def toCelsius(self):
        if self.System == TempSystem.Kelvin:
            res = self.Value - 273.15
        elif self.System == TempSystem.Celsius:
            res = self.Value
        elif self.System == TempSystem.Farenheit:
            res = ((self.Value - 32) / 1.8)
        return round(res * self.Precision) / self.Precision
    def toFahrenheit(self):
        if self.System == TempSystem.Kelvin:
            res = ((self.Value - 273.15) * 1.8) + 32
        elif self.System == TempSystem.Celsius:
            res = (self.Value * 1.8) + 32
        elif self.System == TempSystem.Farenheit:
            res = self.Value
        return round(res * self.Precision) / self.Precision
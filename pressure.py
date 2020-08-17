import measurement

class Pressure(measurement.Measurement):
    def __init__(self, value):
        super().__init__("Pressure")
        self.Data[str(self.Sensor)] = value
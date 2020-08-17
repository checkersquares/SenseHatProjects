import measurement

class Barometer(measurement.Measurement):
    def __init__(self, value):
        self.Sensor = "Pressure"
        self.Value = value
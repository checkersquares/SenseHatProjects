import measurement

class Color(measurement.Measurement):
    def __init__(self, value):
        self.Sensor = "Color"
        self.Value = value
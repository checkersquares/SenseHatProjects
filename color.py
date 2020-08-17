import measurement

class Color(measurement.Measurement):
    def __init__(self, value):
        super().__init__("Color")
        self.Data[str(self.Sensor)] = value
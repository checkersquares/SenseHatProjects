import measurement

class Humidity(measurement.Measurement):
    def __init__(self, value):
        super().__init__("Humidity")
        self.Data[str(self.Sensor)] = value
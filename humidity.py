import measurement

class Humidity(measurement.Measurement):
    def __init__(self, value):
        self.Sensor = "Humidity" 
        self.Value = value
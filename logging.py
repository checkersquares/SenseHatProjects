import datetime
import json
import measurement

class SensorLogEntry():
    def __init__(self, measurement): 
        self.Measurement = measurement
        self.Timestamp = datetime.datetime.now()
        self.save()
        self.log()
    def toString(self):
        res = ""
        res += self.Timestamp.strftime("%H:%M:%S - ")
        res += self.Measurement.Sensor
        for key, value in self.Measurement.Data.items():
            res += " - " + str(key) + ": " + str(value)
        return res
    def toJson(self):
        res = {}
        res["timestamp"] = self.Timestamp.timestamp()
        res["sensor"] = self.Measurement.Sensor
        res["data"] = []
        for key, value in self.Measurement.Data.items():
            res["data"].append({str(key):value})
        return res
    # creates human readble log entries
    def log(self):
        with open("logs/" + self.Timestamp.strftime("%Y-%m-%d_") + self.Measurement.Sensor + "_Log.txt", "a") as logfile:
            logfile.write(self.toString())
            logfile.write("\r")
    # creates json data that can be read and evaluated
    def save(self):
        with open("data/" + self.Measurement.Sensor + "_Data.txt", "a") as jsonfile:
            json.dump(self.toJson(), jsonfile)
            jsonfile.write("\r")
    